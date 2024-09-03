# reesaber-py
Make ReeSaber Presets in Python!

## Usage
Create an empty list variable, this will store every module. At the start of every module creation, pass this variable.

**reesaber-py is designed for 0.3.7+ but could work on other versions. I will not provide support for versions older than 0.3.7.**

### Functions:
```python
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
)
# Returns the module's JSON to be appended to the modules list
```
```python
create_trail(
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
)
# Returns the module's JSON to be appended to the modules list
```
```python
create_vanilla_saber(with_trail=False, name="Vanilla Saber", local_transform=None)
# Returns the module's JSON to be appended to the modules list
```

```python
export(modules, save_to)
# Saves the final ReeSaber preset to a file (save_to is the file path)
```
```python
configLog(level=logging.INFO, filename=datetime.datetime.now() + " - ReeSaber Python.log") 
# Configure logging
```

## Example script
```python
# import for finding the correct folder
import os
# import the functions for creating the saber
import reesaber

# creating the list in which you can put modules
modules = []

# creates a blur saber
modules.append(reesaber.create_blur_saber(saber_thickness=2))
modules.append(reesaber.create_trail())

# exports the modules to reesaber preset
reesaber.export(modules,"saber.json")
```

## License
 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">Reesaber Python</span> by <span property="cc:attributionName">CodeSoft</span> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p> 