import pde


def run_pde(t_range, storage):
    """run a pde and store trajectory"""
    field = pde.ScalarField.random_uniform(pde.UnitGrid([8, 8]))
    eq = pde.DiffusionPDE()
    result = eq.solve(
        field,
        t_range=t_range,
        dt=0.1,
        backend="numpy",
        tracker=pde.ModelrunnerStorage(storage).tracker(1),
    )
    return {"field": result}
