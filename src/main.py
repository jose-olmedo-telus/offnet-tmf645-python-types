from src.models.pending_job.place import Place

if __name__ == "__main__":
    test_obj = {"id":"test_id", "role":"place"}
    test_model = Place.parse_obj(test_obj)
    print(test_model)