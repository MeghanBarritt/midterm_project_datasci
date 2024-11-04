def get_data(filepath):
    import os,json
    import pandas as pd

    all_tags = []
    all_status = []
    all_list_date = []
    all_open_houses = []
    all_year_built = []
    all_baths_3qtr = []
    all_sold_date = []
    all_sold_price = []
    all_baths_full = []
    all_name = []
    all_baths_half = []
    all_lot_sqft = []
    all_sqft = []
    all_baths = []
    all_sub_type = []
    all_baths_1qtr = []
    all_garage = []
    all_stories = []
    all_beds = []
    all_type = []
    all_list_price = []
    all_lead_attrib = []
    all_property_id = []
    all_is_new = []
    all_for_rent = []
    all_is_subdivision = []
    all_is_contingent = []
    all_price_reduced = []
    all_is_pending = []
    all_is_foreclosure = []
    all_is_plan = []
    all_is_coming_soon = []
    all_is_new_listing = []
    all_community = []
    all_products = []
    all_listing_id = []
    all_reduced_amount = []
    all_state = []
    all_city = []

    formatting = ({
        'tags': all_tags,
        'status': all_status,
        'list_date': all_list_date, 
        'open_houses': all_open_houses, 
        'descrip_year_built': all_year_built,
        'descrip_baths_3qtr': all_baths_3qtr,
        'descrip_sold_date': all_sold_date,
        'descrip_sold_price': all_sold_price, 
        'descrip_baths_full': all_baths_full,
        'descrip_name': all_name,
        'descrip_baths_half': all_baths_half, 
        'descrip_lot_sqft': all_lot_sqft,
        'descrip_sqft': all_sqft,
        'descrip_baths': all_baths, 
        'descrip_sub_type': all_sub_type, 
        'descrip_baths_1qtr': all_baths_1qtr, 
        'descrip_garage': all_garage,
        'descrip_stories': all_stories, 
        'descrip_beds': all_beds,
        'descrip_type': all_type,
        'list_price': all_list_price, 
        'lead_attributes': all_lead_attrib, 
        'property_id': all_property_id,
        'flags_is_new_construction': all_is_new,
        'flags_is_for_rent': all_for_rent, 
        'flags_is_subdivision': all_is_subdivision,
        'flags_is_contingent': all_is_contingent,
        'flags_is_price_reduced': all_price_reduced,
        'flags_is_pending': all_is_pending,
        'flags_is_foreclosure': all_is_foreclosure, 
        'flags_is_plan': all_is_plan,
        'flags_is_coming_soon': all_is_coming_soon, 
        'flags_is_new_listing': all_is_new_listing,
        'community': all_community,
        'products': all_products,
        'listing_id': all_listing_id, 
        'price_reduced_amount': all_reduced_amount, 
        'location_state': all_state,
        'location_city': all_city})

    for file in os.listdir(filepath):
        if file.endswith('.json'):
            f = open(filepath+'/'+ file)
            loaded = json.load(f) 
            results = loaded['data']['results']
            
            for entry in results:
                tags = entry['tags']
                status = entry['status']
                list_date = entry['list_date']
                open_houses = entry['open_houses']
                year_built = entry['description']['year_built']
                baths_3qtr = entry['description']['baths_3qtr']
                year_built = entry['description']['year_built']
                baths_3qtr = entry['description']['baths_3qtr']
                sold_date = entry['description']['sold_date']
                sold_price = entry['description']['sold_price']
                baths_full = entry['description']['baths_full']
                name = entry['description']['name']
                baths_half = entry['description']['baths_half']
                lot_sqft = entry['description']['lot_sqft']
                sqft = entry['description']['sqft']
                baths = entry['description']['baths']
                sub_type = entry['description']['sub_type']
                baths_1qtr = entry['description']['baths_1qtr']
                garage = entry['description']['garage']
                stories = entry['description']['stories']
                beds = entry['description']['beds']
                house_type = entry['description']['type']
                list_price = entry['list_price']
                lead_attributes = entry['lead_attributes']
                property_id = entry['property_id']
                is_new_construction = entry['flags']['is_new_construction']
                is_for_rent = entry['flags']['is_for_rent']
                is_subdivision = entry['flags']['is_subdivision']
                is_contingent = entry['flags']['is_contingent']
                is_price_reduced = entry['flags']['is_price_reduced']
                is_pending = entry['flags']['is_pending']
                is_foreclosure = entry['flags']['is_foreclosure']
                is_plan = entry['flags']['is_plan']
                is_coming_soon = entry['flags']['is_coming_soon']
                is_new_listing = entry['flags']['is_new_listing']
                community = entry['community']
                products = entry['products']
                listing_id = entry['listing_id']
                price_reduced_amount = entry['price_reduced_amount']
                state = entry['location']['address']['state']
                city = entry['location']['address']['city']
                
                all_tags.append(tags)
                all_status.append(status)
                all_list_date.append(list_date)
                all_open_houses.append(open_houses)
                all_year_built.append(year_built)
                all_baths_3qtr.append(baths_3qtr)
                all_sold_date.append(sold_date)
                all_sold_price.append(sold_price)
                all_baths_full.append(baths_full)
                all_name.append(name)
                all_baths_half.append(baths_half)
                all_lot_sqft.append(lot_sqft)
                all_sqft.append(sqft)
                all_baths.append(baths)
                all_sub_type.append(sub_type)
                all_baths_1qtr.append(baths_1qtr)
                all_garage.append(garage)
                all_stories.append(stories)
                all_beds.append(beds)
                all_type.append(house_type)
                all_list_price.append(list_price)
                all_lead_attrib.append(lead_attributes)
                all_property_id.append(property_id)
                all_is_new.append(is_new_construction)
                all_for_rent.append(is_for_rent)
                all_is_subdivision.append(is_subdivision)
                all_is_contingent.append(is_contingent)
                all_price_reduced.append(is_price_reduced)
                all_is_pending.append(is_pending)
                all_is_foreclosure.append(is_foreclosure)
                all_is_plan.append(is_plan)
                all_is_coming_soon.append(is_coming_soon)
                all_is_new_listing.append(is_new_listing)
                all_community.append(community)
                all_products.append(products)
                all_listing_id.append(listing_id)
                all_reduced_amount.append(price_reduced_amount)
                all_state.append(state)
                all_city.append(city)

                dataframe = pd.DataFrame(formatting)
            f.close()
    return dataframe



def extract_tags(df):
    import pandas as pd
    tags = df['tags'].values
    tags_dicts = [dict(zip(x,[1]*len(x))) if x is not None else {} for x in tags]
    df_tags = pd.json_normalize(tags_dicts)
    final = pd.concat([df['tags'],df_tags,df.drop('tags',axis=1)],axis=1)

    return final