    return probs

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data_json", help="path to data json")
    parser.add_argument("model_path", help="path to model")
    args = parser.parse_args()
    probs = predict(args.data_json, args.model_path)
