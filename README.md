# Wii U Rich Presence Plugin - Database
Image database for the [Wii U Rich Presence plugin](https://github.com/FlamingNineteen/RichPresenceWUPS).

# Contribute
If there are games that you would like to display on your profile, but are not on this repository, you can help add them! To add games, you will need a <ins>GitHub account</ins>. It is also recommended that you install either [ftpiiu](https://github.com/wiiu-env/ftpiiu_plugin) or [WiiUDownloader](https://github.com/Xpl0itU/WiiUDownloader), and have an image converter like [ImageMagick](https://www.imagemagick.org).

## Invalid Games
Firstly, you should know what games or apps **do not** go in this repository. The following are not suitable for this plugin:

- Virtual Console injects
  - Regular Virtual Console games are allowed
- Applets (Friend List, Browser, Amiibo Settings, etc.)
- vWii and any Wii games
  - Includes Gamecube games from Nintendont
- Homebrew applications
- Games already in this repository

## Setup
To start, clone or fork this repository.

This tutorial will cover three methods of getting game information for the repository:

- **Use the Python scripts:** The easiest way to add games is by using the premade Python scripts in this repository, specifically `ftp.py`. This script requires that you have a Wii U with [ftpiiu](https://github.com/wiiu-env/ftpiiu_plugin). It also requires that the game that you are adding is a digital game, not a physical game.
- **Downloading the game files:** Uses [WiiUDownloader](https://github.com/Xpl0itU/WiiUDownloader) to obtain the necessary files. Great if you don't have a Wii U or a digital copy of the game that you're adding.
- **Manually copying from FTP server:** This method is the same as the Python scripts, just manually. Requires a Wii U with [ftpiiu](https://github.com/wiiu-env/ftpiiu_plugin) and a way for you to connect to and transfer files from an FTP server. It also requires that the game that you are adding is a digital game, not a physical game. Not recommended, as it is very tedious to find the game(s) you are looking for.

## Using the Python Scripts
> [!NOTE]
> This method involves accessing your system's NAND or USB.

Turn on your Wii U, and in the plugin configuration settings, make sure ftpiiu is installed and enabled. Make sure "Allow access to system files" is set to true. Save the configurations.

Run the `ftp.py` Python script in your cloned or forked repository. Enter the IP address of your Wii U (shown in ftpiiu's configuration settings). The Python script will automatically go through your system, downloading only new icons into the `downloads` folder and adding the games to the `titles.json` file.

> [!IMPORTANT]
> This method may also unintentionally transfer Virtual Console injects. Remove any instances of these in the `titles.json` file as well as their icons.

That's it for getting the media! You can skip down to [formatting the icons](#formatting-the-icons).

## Using WiiUDownloader
In WiiUDownloader, you can download decrypted game contents. Select the game(s) you want to add, then toggle "Decrypt contents" before downloading. **Be aware of the game region(s).**

Once the contents are decrypted, open the `meta` folder. `iconTex.tga` is the game's icon. I recommend saving the icons you get in a new folder in your cloned repository, `downloads`.

Additionally, there should be a `meta.xml` file in the `meta` folder. In that file, find the `longname_en` tag. This is the name the plugin uses to match images.

In `titles.json`, add a new key with the same name as the `longname_en` tag. Here is an example for LEGO® Marvel Super Heroes:
```
"LEGO® Marvel Superheroes":"iconTex.tga"
```
That's it for getting the media! You can skip down to [formatting the icons](#formatting-the-icons).

## Manually copying from FTP server
> [!IMPORTANT]
> This method is difficult and not recommended unless you know what you're doing.

> [!NOTE]
> This method involves accessing your system's NAND or USB.

Turn on your Wii U, and in the plugin configuration settings, make sure ftpiiu is installed and enabled. Make sure "Allow access to system files" is set to true. Save the configurations.

Connect to your Wii U's FTP server. The server information can be found in ftpiiu's configuration settings. Then enter `/storage_mlc/usr/title` for games stored on NAND, or `/storage_usb/usr/title` for games stored on a USB. Enter the hexidecimal directories until you see a `meta` directory.

`iconTex.tga` is the game's icon. I recommend saving the icons you get in a new folder in your cloned repository, `downloads`.

Additionally, there should be a `meta.xml` file in the `meta` folder. In that file, find the `longname_en` tag. This is the name the plugin uses to match images.

In `titles.json`, add a new key with the same name as the `longname_en` tag. Here is an example for LEGO® Marvel Super Heroes:
```
"LEGO® Marvel Superheroes":"iconTex.tga"
```
Note that you will probably have to look through the `meta.xml` files of many games before you find the game(s) you are looking for.

## Formatting the Icons
The Python script `to_jpg.py` automatically converts and formats the images in the `downloads` directory into the `icons` directory of your cloned repository for you. However, it requires [ImageMagick](https://www.imagemagick.org).

You can also use any other program to convert the icons to JPG files. **Make sure to upscale them to 512x512**.

Likely right now your icons are named stuff like `iconTex (2).jpg`. Renaming them helps find icons quicker. Open `titles.json`, and edit the values of the keys for the added games. The image names should be short, perhaps abbreviated if the name is long. Here is an example for LEGO® Marvel Super Heroes:
```
"LEGO® Marvel Superheroes":"legomsh.jpg"
```
Once you've changed the keys, rename each image icon accordingly.

## Create a Pull Request
Once you are satisfied with the games you've added, you can double check that they will display correctly before creating a pull request. 

You can execute program using your repository to test out the images. In a command prompt, add `repo [USERNAME]/[REPOSITORY]` as arguments. For example:
```
WURP-Windows repo FlamingNineteen/RichPresenceWUPS-DB
python3 discord-script.py repo FlamingNineteen/RichPresenceWUPS-DB
```

If all looks good, you can create a pull request to the original repository so the icons can get added for everyone to use.
