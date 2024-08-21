# reesaber-py
 Make ReeSaber Presets in Python!
## Usage
Create an empty list variable, this will store every module. At the start of every module creation, pass this variable.

**reesaber-py is designed for 0.3.7+ but could work on other versions. I will not provide support for versions older than 0.3.7.**

### Functions:
create_blur_saber(
    modules, name="Blur Saber", scale_factor=1.0, z_offset_from=-0.17, z_offset_to=1.0,
    saber_thickness=1.0, start_cap=True, end_cap=True, vertical_resolution=20, horizontal_resolution=10,
    blur_frames=2.0, glow_multiplier=1.0, handle_roughness=2.0,
    handle_color=None, blade_mask_resolution=256, drivers_mask_resolution=32,
    cull_mode=0, depth_write=False, render_queue=3002,
    handle_mask=None, blade_mappings=None, drivers_sample_mode=0,
    viewing_angle_mappings=None, surface_angle_mappings=None, local_transform=None, saber_profile = None
) -> Returns the updated module list

export(modules, save_to) -> Saves the final ReeSaber preset to a file (save_to is the file path)

configLog(level=logging.INFO, filename=datetime.datetime.now() + " - ReeSaber Python.log") -> Configure logging
## License
 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">Reesaber Python</span> by <span property="cc:attributionName">CodeSoft</span> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p> 