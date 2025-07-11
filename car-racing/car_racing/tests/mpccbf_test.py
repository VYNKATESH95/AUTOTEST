import pickle
import sympy as sp
import numpy as np
from racing import offboard
from utils import base, racing_env
from utils.constants import *


def racing(args):
    track_layout = args["track_layout"]
    track_spec = np.genfromtxt("data/track_layout/" + track_layout + ".csv", delimiter=",")
    if args["simulation"]:
        track = racing_env.ClosedTrack(track_spec, track_width=1.0)
        # setup ego car
        ego = offboard.DynamicBicycleModel(name="ego", param=base.CarParam(edgecolor="black"), system_param = base.SystemParam())
        mpc_cbf_param = base.MPCCBFRacingParam(vt=0.8)
        ego.set_state_curvilinear(np.zeros((X_DIM,)))
        ego.set_state_global(np.zeros((X_DIM,)))
        if args["zero_noise"]:
            ego.set_zero_noise()
        ego.start_logging()
        ego.set_ctrl_policy(offboard.MPCCBFRacing(mpc_cbf_param, ego.system_param))
        ego.ctrl_policy.set_timestep(0.1)
        ego.set_track(track)
        ego.ctrl_policy.set_track(track)
        # setup surrounding cars
        t_symbol = sp.symbols("t")
        car1 = offboard.NoDynamicsModel(name="car1", param=base.CarParam(edgecolor="orange"))
        car1.set_track(track)
        car1.set_state_curvilinear_func(t_symbol, 0.2 * t_symbol + 4.0, 0.1 + 0.0 * t_symbol)
        car1.start_logging()
        car2 = offboard.NoDynamicsModel(name="car2", param=base.CarParam(edgecolor="orange"))
        car2.set_track(track)
        car2.set_state_curvilinear_func(t_symbol, 0.2 * t_symbol + 10.0, -0.1 + 0.0 * t_symbol)
        car2.start_logging()
        # setup simulation
        simulator = offboard.CarRacingSim()
        simulator.set_timestep(0.1)
        simulator.set_track(track)
        simulator.add_vehicle(ego)
        ego.ctrl_policy.set_racing_sim(simulator)
        simulator.add_vehicle(car1)
        simulator.add_vehicle(car2)
        simulator.sim(sim_time=50.0)
        with open("data/simulator/racing.obj", "wb") as handle:
            pickle.dump(simulator, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open("data/simulator/racing.obj", "rb") as handle:
            simulator = pickle.load(handle)
    if args["plotting"]:
        simulator.plot_simulation()
        simulator.plot_state("ego")
    if args["animation"]:
        simulator.animate(filename="racing", imagemagick=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulation", action="store_true")
    parser.add_argument("--plotting", action="store_true")
    parser.add_argument("--animation", action="store_true")
    parser.add_argument("--track-layout", type=str)
    parser.add_argument("--zero-noise", action="store_true")
    args = vars(parser.parse_args())
    racing(args)
