import mlatom as ml
init_cond_db = ml.data.molecular_database.load('init_10k.json', format='json')# can be found on Figshare



model = ml.models.vecmsani(model_file = 'OMNIP2x_ft_fulvene.pt', nstates=2)
timemax = 60 # fs
namd_kwargs = {
            'model': model,
            'filename': 'traj.h5',
            'reduce_memory_usage': True,
            'time_step': 0.1, # fs
            'maximum_propagation_time': timemax,
            'hopping_algorithm': 'LZBL',
            'nstates': 2,
            'reduce_kinetic_energy': True,
            'dump_trajectory_interval': 20,
            'initial_state': 1,
            }

dyns = ml.simulations.run_in_parallel(molecular_database=init_cond_db[:1000], task=ml.namd.surface_hopping_md, task_kwargs=namd_kwargs, create_and_keep_temp_directories=True)

ml.namd.plot_population_from_disk(ntraj=1000, time_step=0.1, max_propagation_time=60.0, nstates=2, filename='fulvene.png', 
pop_filename='fulvene.txt',dirname="job_surface_hopping_md_",traj_filename="traj.h5" )

