import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Jackett, Sonarr and BTSync')
    parser.add_argument('jackett-port', type=int, default=9117 help='External facing port for Jackett.')
    parser.add_argument('sonarr-port', type=int, default=8989 help='External facing port for Sonarr.')
    parser.add_argument('btsync-port', type=int, default=9888 help='External facing port for BTSync.')

    parser.add_argument('jackett-dir', type=string, required=True help='Base directory for Jackett files.')
    parser.add_argument('sonarr-dir', type=string, required=True help='Base directory for Sonarr files.')
    parser.add_argument('btsync-dir', type=string, required=True help='Base directory for BTSync files.')
    parser.add_argument('tv-dir', type=string, required=True help='Base directory for TV shows.')

    args = parser.parse_args()
    print(args)
