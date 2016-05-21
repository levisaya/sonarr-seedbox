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
    parser = argparse.ArgumentParser(description='Run Jackett, Sonarr and BTSync')
    parser.add_argument('--jackett-port', type=int, default=9117, help='External facing port for Jackett.')
    parser.add_argument('--sonarr-port', type=int, default=8989, help='External facing port for Sonarr.')
    parser.add_argument('--btsync-port', type=int, default=9888, help='External facing port for BTSync.')

    parser.add_argument('--jackett-dir', type=str, help='Base directory for Jackett files.', required=True)
    parser.add_argument('--sonarr-dir', type=str, help='Base directory for Sonarr files.', required=True)
    parser.add_argument('--btsync-dir', type=str, help='Base directory for BTSync files.', required=True)
    parser.add_argument('--tv-dir', type=str, help='Base directory for TV shows.', required=True)

    args = parser.parse_args()

    print(args)

    main(str(args.jackett_port),
         str(args.sonarr_port),
         str(args.btsync_port),
         args.jackett_dir,
         args.sonarr_dir,
         args.btsync_dir,
         args.tv_dir)
