import logging
import json

experimental = False
if experimental:
    print(
        "This is an experimental version, expect bugs. Do not report them to the issues tab!\n"
    )

# EVERY ReeSaber Driver
TipVelocity = 1
SwingsperSecond = 2
TimeDependence = 3
TipAcceleration = 4
AngularVelocity = 5
ScorePercentage = 6
Combo = 7
Misses = 8
Energy = 9
Multiplier = 10
CutScore = 11
CutAccScore = 12
CutPreScore = 13
CutPostScore = 14
CutsPerSecond = 15
TimeAfterCut = 16
DirectionX = 17
DirectionY = 18
DirectionZ = 19
# im hoping i didnt forget any


class Driver:
    def __init__(self, type, mappings=None, resistance=(0, 0), range=(0, 1)):
        self.type = type  # Should always be a number
        if self.type is None:
            self.type = 0
        self.resistance = resistance
        self.mappings = mappings or {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {
                        "time": 1.0,
                        "value": {"r": 1.0, "g": 0.0, "b": 0.0, "a": 0.2099508},
                    }
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": 1.0},
                    {"time": 1.0, "value": 1.0},
                ],
            },
        }
        self.range = range

    def to_dict(self):
        """Returns a dictionary in the proper ReeSabers JSON format for this driver."""
        return {
            "valueType": self.type,
            "increaseResistance": self.resistance[0],
            "decreaseResistance": self.resistance[1],
            "mappings": self.mappings,
        }


def configLog(level=logging.INFO, filename="ReeSaber Python.log"):
    logging.basicConfig(
        filename=filename,
        level=level,
        format="%(asctime)s - [%(levelname)s] - %(message)s",
    )


def create_blur_saber(
    name="Blur Saber",
    scale_factor=1.0,
    z_offset_from=-0.17,
    z_offset_to=1.0,
    saber_thickness=1.0,
    start_cap=True,
    end_cap=True,
    vertical_resolution=20,
    horizontal_resolution=10,
    blur_frames=2.0,
    glow_multiplier=1.0,
    handle_roughness=2.0,
    handle_color=None,
    blade_mask_resolution=256,
    drivers_mask_resolution=32,
    cull_mode=0,
    depth_write=False,
    render_queue=3002,
    handle_mask=None,
    blade_mappings=None,
    drivers_sample_mode=0,
    viewing_angle_mappings=None,
    surface_angle_mappings=None,
    local_transform=None,
    saber_profile=None,
    drivers=None,
):
    if drivers is None:
        drivers = [
            Driver(None, None),
            Driver(None, None),
            Driver(None, None),
            Driver(None, None),
        ]
    if handle_color is None:
        handle_color = {"r": 0.1, "g": 0.1, "b": 0.1, "a": 0.0}

    if handle_mask is None:
        handle_mask = {
            "interpolationType": 2,
            "controlPoints": [
                {"time": 0.0, "value": 0.0},
                {"time": 0.028, "value": 1.0},
                {"time": 0.128, "value": 0.0},
                {"time": 0.145, "value": 1.0},
                {"time": 0.17, "value": 0.0},
            ],
        }

    if blade_mappings is None:
        blade_mappings = {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}}
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "valueFrom": 0.0,
            "valueTo": 1.0,
        }

    if viewing_angle_mappings is None:
        viewing_angle_mappings = {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}}
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "valueFrom": 0.0,
            "valueTo": 1.0,
        }

    if surface_angle_mappings is None:
        surface_angle_mappings = {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}}
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "valueFrom": 0.0,
            "valueTo": 1.0,
        }

    if local_transform is None:
        local_transform = {
            "Position": {"x": 0, "y": 0, "z": 0},
            "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Scale": {"x": scale_factor, "y": scale_factor, "z": scale_factor},
        }

    if saber_profile is None:
        saber_profile = {
            "interpolationType": 1,
            "controlPoints": [{"time": 0.0, "value": 1.0}, {"time": 1.0, "value": 1.0}],
        }

    toReturn = {
        "ModuleId": "reezonate.blur-saber",
        "Version": 1,
        "Config": {
            "SaberSettings": {
                "zOffsetFrom": z_offset_from,
                "zOffsetTo": z_offset_to,
                "thickness": saber_thickness,
                "saberProfile": saber_profile,
                "startCap": start_cap,
                "endCap": end_cap,
                "verticalResolution": vertical_resolution,
                "horizontalResolution": horizontal_resolution,
                "renderQueue": render_queue,
                "cullMode": cull_mode,
                "depthWrite": depth_write,
                "blurFrames": blur_frames,
                "glowMultiplier": glow_multiplier,
                "handleRoughness": handle_roughness,
                "handleColor": handle_color,
                "maskSettings": {
                    "bladeMaskResolution": blade_mask_resolution,
                    "driversMaskResolution": drivers_mask_resolution,
                    "handleMask": handle_mask,
                    "bladeMappings": blade_mappings,
                    "driversSampleMode": drivers_sample_mode,
                    "viewingAngleMappings": viewing_angle_mappings,
                    "surfaceAngleMappings": surface_angle_mappings,
                    "drivers": [driver.to_dict() for driver in drivers],
                },
            },
            "Enabled": True,
            "Name": name,
            "LocalTransform": local_transform,
        },
    }
    return toReturn


def create_trail(
    name="Simple Trail",
    scale_factor=1.0,
    length=0.16,
    trail_type=1,
    horizontal_res=4,
    vertical_res=60,
    material_type=1,
    offset=1.0,
    width=1.0,
    mask_res=128,
    driver_mask_res=32,
    render_queue=3000,
    anim_layout=None,
    length_mappings=None,
    width_mappings=None,
    drivers_sample_mode=0,
    always_on_top=False,
    blending_mode=0,
    viewing_angle_mappings=None,
    surface_angle_mappings=None,
    local_transform=None,
    drivers=[
        Driver(None, None),
        Driver(None, None),
        Driver(None, None),
        Driver(None, None),
    ],
):

    if viewing_angle_mappings is None:
        viewing_angle_mappings = {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}}
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "valueFrom": 0.0,
            "valueTo": 1.0,
        }

    if surface_angle_mappings is None:
        surface_angle_mappings = {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}}
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "valueFrom": 0.0,
            "valueTo": 1.0,
        }

    if local_transform is None:
        local_transform = {
            "Position": {"x": 0, "y": 0, "z": 0},
            "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Scale": {"x": scale_factor, "y": scale_factor, "z": scale_factor},
        }

    if length_mappings is None:
        length_mappings = {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}}
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "valueFrom": 0.0,
            "valueTo": 1.0,
        }

    if width_mappings is None:
        width_mappings = {
            "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                    {"time": 0.0, "value": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}}
                ],
            },
            "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [{"time": 0.0, "value": 1.0}],
            },
            "valueFrom": 0.0,
            "valueTo": 1.0,
        }

    if anim_layout is None:
        anim_layout = {
            "totalFrames": 1,
            "framesPerRow": 1,
            "framesPerColumn": 1,
            "frameDuration": 1.0,
        }

    toReturn = {
        "ModuleId": "reezonate.simple-trail",
        "Version": 1,
        "Config": {
            "MeshSettings": {
                "TrailLength": length,
                "HorizontalResolution": horizontal_res,
                "VerticalResolution": vertical_res,
            },
            "MaterialSettings": {
                "trailType": trail_type,
                "materialType": material_type,
                "offset": offset,
                "width": width,
                "distortionMultiplier": 1.0,
                "generalSettings": {
                    "customTextureId": "",
                    "animationLayout": anim_layout,
                    "blendingMode": blending_mode,
                    "alwaysOnTop": always_on_top,
                    "renderQueue": render_queue,
                },
                "maskSettings": {
                    "mainMaskResolution": mask_res,
                    "driversMaskResolution": driver_mask_res,
                    "lengthMappings": length_mappings,
                    "widthMappings": width_mappings,
                    "driversSampleMode": drivers_sample_mode,
                    "viewingAngleMappings": viewing_angle_mappings,
                    "surfaceAngleMappings": surface_angle_mappings,
                    "drivers": [driver.to_dict() for driver in drivers],
                },
            },
            "Enabled": True,
            "Name": name,
            "LocalTransform": local_transform,
        },
    }
    return toReturn


def create_vanilla_saber(with_trail=False, name="Vanilla Saber", local_transform=None):

    if local_transform is None:
        local_transform = {
            "Position": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Scale": {"x": 1.0, "y": 1.0, "z": 1.0},
        }

    toReturn = {
        "ModuleId": "reezonate.vanilla-saber",
        "Version": 1,
        "Config": {
            "WithTrail": with_trail,
            "Enabled": True,
            "Name": name,
            "LocalTransform": local_transform,
        },
    }

    return toReturn


def export(modules, save_to):
    saber_json = {
        "ModVersion": "0.3.9",
        "Version": 1,
        "LocalTransform": {
            "Position": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Scale": {"x": 1.0, "y": 1.0, "z": 1.0},
        },
        "Modules": modules,
    }
    try:
        with open(save_to, "w") as f:
            f.write(json.dumps(saber_json, indent=2))
    except Exception as e:
        logging.error(f"export(): {e}")
