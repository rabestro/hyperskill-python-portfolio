from .cli import build_parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    output_message = args.func(args)
    if output_message:
        print(output_message)


if __name__ == "__main__":
    main()
