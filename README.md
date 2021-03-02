# ShopAdder
Simple program for adding item entries to Unprotesting's [Auto-Tune plugin](https://github.com/Unprotesting/Auto-Tune/).

## How do I use it?
There are **2** modes you can use: either manual (data entry) or CSV import.
The CSV import is still being added, so for now manual is the only option.

### Both modes
Before you are asked for the mode you would like to use, you will be asked for the path to your `shops.yml` file, e.g. `D:/Users/felix/Downloads/shops.yml`.
I **strongly recommend** using a copy of the original `shops.yml` file in case of any issues, and once you have finished you can copy it back into the Auto-Tune plugin directory.

Final note: The category you have assigned each item *will not* be added by the program. You must either use the pre-existing categories or add the new categories yourself. This may be a feature in the future, but for now it must be done manually.

### Manual mode
You will be asked for the **line number** that you wish to start adding items from. The line number should be that of a ***blank line directly below the last item in the file***. Below you can see an example `shops.yml` file and a demonstration of the line number that the program should start adding items from.
