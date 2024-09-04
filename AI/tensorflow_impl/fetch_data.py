        except OSError as e:
            if e.errno == errno.ENOENT:
                print("rdsamp not installed, link to the installation guide in the README")
                return False

        print("rdsamp installed check failed")
        return False

    def remove_unwanted_datasets():
        if dataset_list:
            unwanted_ds = physionet.keys() - dataset_list
            for ds in unwanted_ds:
                physionet.pop(ds, None)


    remove_unwanted_datasets()
    check_folder_existance()
