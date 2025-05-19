# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for Unitree robots.

The following configurations are available:

* :obj:`H1v2_CFG`: H1 version 2 humanoid robot
* :obj:`H1v2_MINIMAL_CFG`: H1 version 2 humanoid robot with minimal collision bodies

Reference: https://github.com/unitreerobotics/unitree_ros
"""

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import (
    DelayedPDActuatorCfg,
    ImplicitActuatorCfg,
    IdealPDActuatorCfg,
)
from omni.isaac.lab.assets.articulation import ArticulationCfg


H1v2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        #usd_path=f"/home/atrovatell/ws/constraints-as-terminations/exts/cat_envs/cat_envs/assets/Robots/unitree/h1-v2_description/usd_12dof/h1_2_handless_12dof.usd",
        usd_path=f"/lustre/fswork/projects/rech/ahr/urp31br/constraints-as-terminations/exts/cat_envs/cat_envs/assets/Robots/unitree/h1-v2_description/usd_12dof/h1_2_handless_12dof.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.05),
        joint_pos={
            ".*_hip_yaw_joint": 0.0,
            ".*_hip_roll_joint": 0.0,
            ".*_hip_pitch_joint": -0.16,  # -0.28 -16 degrees
            ".*_knee_joint": 0.36,  # 0.79 45 degrees
            ".*_ankle_pitch_joint": -0.2,  # -0.52 -30 degrees
            ".*_ankle_roll_joint": 0.0,
            #"torso_joint": 0.0,
            # ".*_shoulder_pitch_joint": 0.0, # 0.28
            # ".*_shoulder_roll_joint": 0.0,
            # ".*_shoulder_yaw_joint": 0.0,
            # ".*_elbow_joint": 0.0, # 0.52
            # ".*_wrist_yaw_joint": 0.0,
            # ".*_wrist_roll_joint": 0.0,
            # ".*_wrist_pitch_joint": 0.0,


        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_yaw_joint",
                ".*_hip_roll_joint",
                ".*_hip_pitch_joint",
                #"torso_joint",
            ],
            effort_limit=220,
            velocity_limit=100.0,
            stiffness={
                ".*_hip_yaw_joint": 200.0, 
                ".*_hip_roll_joint": 200.0,
                ".*_hip_pitch_joint": 200.0,
                #"torso_joint": 200.0,
            },
            damping={
                ".*_hip_yaw_joint": 2.5,
                ".*_hip_roll_joint": 2.5,
                ".*_hip_pitch_joint": 2.5,
                #"torso_joint": 5.0,
            },
        ),
        "knees": ImplicitActuatorCfg(
            joint_names_expr=[".*_knee_joint"],
            effort_limit=360,
            velocity_limit=100.0,
            stiffness={
                ".*_knee_joint": 300.0, 
            },
            damping={
                ".*_knee_joint": 4.0,
            },
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[".*_ankle_pitch_joint", ".*_ankle_roll_joint"],
            effort_limit=45,
            velocity_limit=100.0,
            stiffness={
                ".*_ankle_pitch_joint": 40.0,
                ".*_ankle_roll_joint": 40.0,
            },
            damping={
                ".*_ankle_pitch_joint": 2.0,
                ".*_ankle_roll_joint": 2.0,
            },
        ),
        #"arms": ImplicitActuatorCfg(
        # "arms": DelayedPDActuatorCfg(
        #     joint_names_expr=[".*_shoulder_pitch_joint", ".*_shoulder_roll_joint", ".*_shoulder_yaw_joint", ".*_elbow_joint", ".*_wrist_yaw_joint", ".*_wrist_roll_joint", ".*_wrist_pitch_joint"],
        #     effort_limit=75,
        #     velocity_limit=100.0,
        #     stiffness={
        #         ".*_shoulder_pitch_joint": 40.0,
        #         ".*_shoulder_roll_joint": 40.0,
        #         ".*_shoulder_yaw_joint": 40.0,
        #         ".*_elbow_joint": 40.0,
        #         ".*_wrist_yaw_joint": 40.0,
        #         ".*_wrist_roll_joint": 40.0,
        #         ".*_wrist_pitch_joint": 40.0,
        #     },
        #     damping={
        #         ".*_shoulder_pitch_joint": 10.0,
        #         ".*_shoulder_roll_joint": 10.0,
        #         ".*_shoulder_yaw_joint": 10.0,
        #         ".*_elbow_joint": 10.0,
        #         ".*_wrist_yaw_joint": 10.0,
        #         ".*_wrist_roll_joint": 10.0,
        #         ".*_wrist_pitch_joint": 10.0,
        #     },
        # ),
    },
)
H1v2_MINIMAL_CFG = H1v2_CFG.copy()
