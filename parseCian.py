import cianparser


def findFlats(numOfRooms):
    spb_parser = cianparser.CianParser(location="Санкт-Петербург")

    data = spb_parser.get_flats(deal_type="rent_long",
                                rooms=numOfRooms,
                                additional_settings={"start_page":1, "end_page":20},
                                with_saving_csv=True)
    return data

findFlats(1) # this creates a .csv file with info about flats from cian