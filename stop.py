import argparse
import subprocess, os

def main(jackett_port,
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

    subprocess.Popen(['docker-compose', 'stop'], env=env)

if __name__ == "__main__":
    json_config = {
      "jackett_port": None,
      "sonarr_port":  None,
      "btsync_port":  None,
      "jackett_dir":  None,
      "sonarr_dir":   None,
      "btsync_dir":   None,
      "tv_dir":       None
    }

    try:
        with open('config.json', 'r') as json_file:
            json_config = json.load(json_file)
    except:
        pass

    parser = argparse.ArgumentParser(description='Run Jackett, Sonarr and BTSync')
    parser.add_argument('--jackett-port', type=int, default=json_config.get('jackett_port', None), help='External facing port for Jackett.')
    parser.add_argument('--sonarr-port', type=int, default=json_config.get('sonarr_port', None), help='External facing port for Sonarr.')
    parser.add_argument('--btsync-port', type=int, default=json_config.get('btsync_port', None), help='External facing port for BTSync.')

    parser.add_argument('--jackett-dir', type=str, default=json_config.get('jackett_dir', None), help='Base directory for Jackett files.')
    parser.add_argument('--sonarr-dir', type=str, default=json_config.get('sonarr_dir', None), help='Base directory for Sonarr files.')
    parser.add_argument('--btsync-dir', type=str, default=json_config.get('btsync_dir', None), help='Base directory for BTSync files.')
    parser.add_argument('--tv-dir', type=str, default=json_config.get('tv_dir', None), help='Base directory for TV shows.')

    args = vals(parser.parse_args())

    if None in args.values():
        for argname, argval in args.items():
            print("{} not specified in the config json or on the command line, exiting!")
        exit(1)

    main(str(args.jackett_port),
         str(args.sonarr_port),
         str(args.btsync_port),
         args.jackett_dir,
         args.sonarr_dir,
         args.btsync_dir,
         args.tv_dir)

