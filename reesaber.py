from PIL import ImageFont, Image, ImageDraw
import colorama
import json


def create_blur_saber(
    modules, name="Blur Saber", scale_factor=1.0, z_offset_from=-0.17, z_offset_to=1.0,
    saber_thickness=1.0, start_cap=True, end_cap=True, vertical_resolution=20, horizontal_resolution=10,
    blur_frames=2.0, glow_multiplier=1.0, handle_roughness=2.0,
    handle_color=None, blade_mask_resolution=256, drivers_mask_resolution=32,
    cull_mode=0, depth_write=False, render_queue=3002,
    handle_mask=None, blade_mappings=None, drivers_sample_mode=0,
    viewing_angle_mappings=None, surface_angle_mappings=None, local_transform=None, saber_profile = None
):
    if handle_color is None:
        handle_color = {"r": 0.1, "g": 0.1, "b": 0.1, "a": 0.0}

    if handle_mask is None:
        handle_mask = {
              "interpolationType": 2,
              "controlPoints": [
                {
                  "time": 0.0,
                  "value": 0.0
                },
                {
                  "time": 0.028,
                  "value": 1.0
                },
                {
                  "time": 0.128,
                  "value": 0.0
                },
                {
                  "time": 0.145,
                  "value": 1.0
                },
                {
                  "time": 0.17,
                  "value": 0.0
                }
              ]
            }

    if blade_mappings is None:
        blade_mappings = {
              "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": {
                      "r": 1.0,
                      "g": 1.0,
                      "b": 1.0,
                      "a": 1.0
                    }
                  }
                ]
              },
              "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": 1.0
                  }
                ]
              },
              "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": 1.0
                  }
                ]
              },
              "valueFrom": 0.0,
              "valueTo": 1.0
            }

    if viewing_angle_mappings is None:
        viewing_angle_mappings = {
              "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": {
                      "r": 1.0,
                      "g": 1.0,
                      "b": 1.0,
                      "a": 1.0
                    }
                  }
                ]
              },
              "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": 1.0
                  }
                ]
              },
              "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": 1.0
                  }
                ]
              },
              "valueFrom": 0.0,
              "valueTo": 1.0
            }

    if surface_angle_mappings is None:
        surface_angle_mappings = {
              "colorOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": {
                      "r": 1.0,
                      "g": 1.0,
                      "b": 1.0,
                      "a": 1.0
                    }
                  }
                ]
              },
              "alphaOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": 1.0
                  }
                ]
              },
              "scaleOverValue": {
                "interpolationType": 0,
                "controlPoints": [
                  {
                    "time": 0.0,
                    "value": 1.0
                  }
                ]
              },
              "valueFrom": 0.0,
              "valueTo": 1.0
            }

    if local_transform is None:
        local_transform = {
                "Position": {
                    "x": 0,
                    "y": 0,
                    "z": 0
                },
                "Rotation": {
                    "x": 0.0,
                    "y": 0.0,
                    "z": 0.0
                },
                "Scale": {
                    "x": scale_factor,
                    "y": scale_factor,
                    "z": scale_factor
                }
            }

    if saber_profile is None:
        saber_profile = {
                    "interpolationType": 1,
                    "controlPoints": [
                        {"time": 0.0, "value": 1.0},
                        {"time": 1.0, "value": 1.0}
                    ]
                }

    modules.append({
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
                    "drivers": [] # TODO: Add driver support
                }
            },
            "Enabled": True,
            "Name": name,
            "LocalTransform": local_transform
            }
        })
    return modules

def export(modules, save_to):
    saber_json = {
        "ModVersion": "0.3.9",
        "Version": 1,
        "LocalTransform": {
            "Position": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0},
            "Scale": {"x": 1.0, "y": 1.0, "z": 1.0}
        },
        "Modules": modules
    }
    try:
        with open(save_to, "w") as f:
            f.write(json.dumps(saber_json, indent=2))
    except Exception as e:
        print(f"An error occurred while saving this ReeSaber preset, see below.\n{colorama.Fore.RED}[ERROR]{colorama.Style.RESET_ALL} {e}")
