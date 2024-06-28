    pbar.update(1)


if __name__ == "__main__":
    p = mp.Pool(processes=mp.cpu_count())
    p.map(run, ecg_data)
