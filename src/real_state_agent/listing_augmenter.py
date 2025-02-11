class ListingAugmenter:
    def __init__(self, llm):
        self.llm = llm

    def _augment_listing(self, listing_description, buyer_preferences):
        prompt_template = """
        You are a real estate assistant. Your task is to augment the property listing description to resonate with the buyer's specific preferences.
        STRICT RULES:
        1. DO NOT alter or invent any factual information provided in [Original Listing]. 
           - This includes details like the number of bedrooms, bathrooms, price, house size, and neighborhood.
           - Use these details EXACTLY as provided in the listing.
        2. If the buyer's preferences mention features that are NOT in the listing, DO NOT include them in the augmented description.
        3. Only emphasize aspects of the property that align with the buyer's preferences, without adding new data.

        Buyer Preferences:
        {buyer_preferences}

        [Original Listing]:
        {listing_description}

        Augmented Listing:
        """
        prompt = prompt_template.format(
            buyer_preferences=buyer_preferences,
            listing_description=listing_description,
        )
        augmented_description = self.llm.invoke(prompt)
        return augmented_description

    def _augment_listings(self, listings, buyer_preferences):
        augmented_listings = []
        for listing in listings:
            listing_description = '\n'.join(listing['text'].splitlines()[3:])
            augmented_description = self._augment_listing(listing_description,
                                                          buyer_preferences)
            augmented_listings.append(augmented_description)
        return augmented_listings

    def process(self, listings, buyer_preferences):
        augmented_listings = self._augment_listings(listings,
                                                    buyer_preferences)
        return augmented_listings
