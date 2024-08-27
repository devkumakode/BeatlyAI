
if __name__ == "__main__":
    args = parse_args()
    config = json.loads(open(args.config).read())
    pipeline_type = getattr(pipelines, config["type"])

    print("Trainer: ", config["type"], pipeline_type)
