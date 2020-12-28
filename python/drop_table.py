for i in range(100):
    print(
        f"bq query --nouse_legacy_sql 'DROP TABLE `sas-saude-evol-plataforma1.dataset_datastream.Z_TEST_{str(i+1).zfill(3)}`' ")
