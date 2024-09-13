                subprocess.check_call(cmd, shell=True)
            except Exception as e:
                print("Failed to execute command: {} with exception: {}".format(cmd, e))
                if os.path.exists(csv_file_path):
                    os.remove(csv_file_path)

        if os.path.isdir(database_dir) and not os.listdir(database_dir):
            cmd = "rm -rf {}".format(database_dir)
