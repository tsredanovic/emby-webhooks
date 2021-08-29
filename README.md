# Emby Webhooks

Service which catches emby webhooks, generates messages and sends Discord notifications.


## Installation

1. Clone this repository

2. `cd` into the root directory
```
cd emby-webhooks
```

3. Create a python virtual environment
```bash
python3 -m venv venv
```

4. Activate the created virtual environment
```bash
source venv/bin/activate
```

5. Install requirements
```bash
pip install -r requirements.txt
```


## Configuration

1. Create a discord webhook as explained [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

2. Create a `config.json` file next to the `main.py` file in `emby-webhooks` repository. 
`config.json` file must contain:
    - `discord_webhook_urls` - list of discord webhook URLs (multiple are supported, but one is enough)

`config.json` example:
```json
{
    "discord_webhook_urls": [
        "_your_discord_webhook_url_"
    ]
}
```


## Events

### System events

- Server updates
  - **Event:** ???
  - **Trigger:** ???
  - **Template file:** -
  - **Default message:** -

- Plugin updates
  - **Event:** ???
  - **Trigger:** ???
  - **Template file:** -
  - **Default message:** -

### Playback events

- Playback start
  - **Event:** `playback.start`
  - **Trigger:** Media file starts playing.
  - **Template file:** `templates/playback.start.txt`
  - **Default message:** User `{username}` started `{filename}`.

- Playback pause
  - **Event:** `playback.pause`
  - **Trigger:** Media file playback is paused.
  - **Template file:** `templates/playback.pause.txt`
  - **Default message:** User `{username}` paused `{filename}`.

- Playback resume
  - **Event:** `playback.unpause`
  - **Trigger:** Media file playback is resumed.
  - **Template file:** `templates/playback.unpause.txt`
  - **Default message:** User `{username}` unpaused `{filename}`.

- Playback stop
  - **Event:** `playback.stop`
  - **Trigger:** Media file playback is stopped.
  - **Template file:** `templates/playback.stop.txt`
  - **Default message:** User `{username}` stopped `{filename}`.

- Playback scrobble
  - **Event:** ???
  - **Trigger:** ???
  - **Template file:** -
  - **Default message:** -

### User events

- Mark favorites
  - **Event:** `item.rate`
  - **Trigger:** User marks media either as favourite or unfavourite.
  - **Template file:** `templates/item.rate.txt`
  - **Default message:** User `{username}` marked `{filename}` as `Favourite` or `Unfavourite`.

- Mark Played
  - **Event:** `item.markplayed`
  - **Trigger:** User marks media as played.
  - **Template file:** `templates/item.markplayed.txt`
  - **Default message:** User `{username}` marked `{filename}` as `Played`.

- Mark Unplayed
  - **Event:** `item.markunplayed`
  - **Trigger:** User marks media as unplayed.
  - **Template file:** `templates/item.markunplayed.txt`
  - **Default message:** User `{username}` marked `{filename}` as `Unplayed`.

### Other events

- Send Test Webhook
  - **Event:** `system.webhooktest`
  - **Trigger:** Sending test webhook.
  - **Template file:** `templates/system.webhooktest.txt`
  - **Default message:** Got event `{event}` from server `{servername}` with ID: `{serverid}`.


## Messages

Messages are generated using the [Jinja](https://jinja.palletsprojects.com/) templating engine. 

A message template for each event must be located inside the `templates` directory with the following naming syntax: `{Event}.txt`.

Default templates are provided for some events as described in the [Events](#events) section. Each of them can be customized (or new ones added) to your liking by following the Jinja's [Template Designer Documentation](https://jinja.palletsprojects.com/templates/).


## Running

1. Create systemd service file `/etc/systemd/system/embyhooks.service`
    ```service
    sudo nano /etc/systemd/system/embyhooks.service
    ```

    Replace `/full/path/to/` with full path to `emby-webhooks` cloned repository and `root` to user which runs the service (if appropriate). Then, after saving the file, you need to reload systemd's daemons: `sudo systemctl daemon-reload`. 
    
    The content of the file is:
    ```conf
    [Unit]
    Description=Emby webhooks
    After=network.target

    [Service]
    Type=simple
    User=root
    Group=root
    WorkingDirectory=/full/path/to/emby-webhooks/
    ExecStart=/full/path/to/emby-webhooks/venv/bin/gunicorn run:app -b 0.0.0.0:64921
    Restart=always
    RestartSec=3

    [Install]
    WantedBy=multi-user.target
    ```

    This will run the service available on your local network with device's local IP address and port `64921`. If you want to have the service available only on the device (localhost) you should change `0.0.0.0` to `127.0.0.1`. To switch to another port replace `64921` with whichever port number you want (just make sure it is available).

2. Enable service start on system boot
    ```bash
    sudo systemctl enable embyhooks.service
    ```

3. Using the service
    - `sudo systemctl status embyhooks.service` - show service status
    - `sudo systemctl start embyhooks.service` - start the service
    - `sudo systemctl stop embyhooks.service` - stop the service

## License

**Emby Webhooks** is a free software under terms of the `MIT License`.

Copyright (C) 2021 by [Toni Sredanović](https://tsredanovic.github.io/), toni.sredanovic@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
