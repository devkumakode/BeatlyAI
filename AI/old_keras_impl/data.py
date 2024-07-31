                        reader.next()
                        for row in reader:
                            csvwriter.writerow([row[1]])