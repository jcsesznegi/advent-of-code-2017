

from swarm import Swarm

def test_get_closest_particle():
    positions = ([
        [3,0,0],
        [4,0,0],
    ])

    velocities = ([
        [2,0,0],
        [0,0,0],
    ])

    accelerations = ([
        [-1,0,0],
        [-2,0,0],
    ])

    s = Swarm(positions, velocities, accelerations)

    s.run(10)

    assert s.getClosestParticleIndex() == 0
