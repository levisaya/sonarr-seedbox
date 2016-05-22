import argparse
import subprocess, os
import json

def main(command,
         jackett_port,
         sonarr_port,
         btsync_port,
         jackett_dir,
         sonarr_dir,
         btsync_dir,
         tv_dir):
    env = os.environ.copy()
    env['JACKETT_PORT'] = jackett_port
    env['SONARR_PORT'] = sonarr_port
    env['BTSYNC_PORT'] = btsync_port
    env['JACKETT_DIR'] = jackett_dir
    env['SONARR_DIR'] = sonarr_dir
    env['BTSYNC_DIR'] = btsync_dir
    env['TV_DIR'] = tv_dir

    if command.lower() in ['start']:
        subprocess.Popen(['docker-compose', 'up', '-d'], env=env)
    elif command.lower() in ['stop']:
        subprocess.Popen(['docker-compose', 'stop'], env=env)
    else:
        print "Command unknown."

if __name__ == "__main__":
    # Load settings from config.json
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    parser = argparse.ArgumentParser(description='Run Jackett, Sonarr and BTSync')

    # The point of this file
    parser.add_argument('command', type=str, help='The command to run. start or stop', default='start')

    # Ports
    parser.add_argument('--jackett-port', type=int, help='External facing port for Jackett.', default=config['jackett_port'])
    parser.add_argument('--sonarr-port', type=int, help='External facing port for Sonarr.', default=config['sonarr_port'])
    parser.add_argument('--btsync-port', type=int, help='External facing port for BTSync.', default=config['btsync_port'])

    # Directories
    parser.add_argument('--jackett-dir', type=str, help='Base directory for Jackett files.', default=config['jackett_dir'])
    parser.add_argument('--sonarr-dir', type=str, help='Base directory for Sonarr files.', default=config['sonarr_dir'])
    parser.add_argument('--btsync-dir', type=str, help='Base directory for BTSync files.', default=config['btsync_dir'])
    parser.add_argument('--tv-dir', type=str, help='Base directory for TV shows.', default=config['tv_dir'])

    args = parser.parse_args()

    print(args)

    main(args.command,
         str(args.jackett_port),
         str(args.sonarr_port),
         str(args.btsync_port),
         args.jackett_dir,
         args.sonarr_dir,
         args.btsync_dir,
         args.tv_dir)
