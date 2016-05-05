{
    event: {
        "display_title": "",
        "subtitle": "",
        "capacity": 0,
        "current_fill": 0,
        "attendee_min_age": 21,
        "lat": "",
        "lon": "",
        "point": "()",
        "venue_id": 3,
        "event_directions": "",
        "private": "",
        "date": DateTime,
        "external_url":,
        "indoor":,
        "outdoor":,
        "organizer":,
        "host_name":,
        "music_genre_id":,
        "performance_type_id":,
        "start_time":,
        "end_time":,
        "dress_type_id":,
    }
}
has_many :event_categories
has_many :attendees
has_one :venue


{
    attendee: {
        "first_name": "",
        "last_name": "",
        "email": "",
        "phone": 0,
        "birthday": 0,
        "external_url":,
        "display_photo_url":,
    }
}
has_many :events
has_many :friends
has_many :favorite_venues
has_many :payment_methods


{
    venue: {
        "display_title": "",
        "subtitle": "",
        "capacity": 0,
        "current_fill": 0,
        "opening_hours_id":,
        "lat": "",
        "lon": "",
        "point": "()",
        "venue_directions": "",
        "external_url":,
        "indoor":,
        "outdoor":,
        "management_company":,
        "accepts_credit_card":
    }
}
has_many :venue_categories

ENUM: {
    event_category: {
        "display_title": "",
        "subtitle": "",
        "constant": ""
    }
}

ENUM: {
    venue_category: {
        "display_title": "",
        "subtitle": "",
        "constant": ""
    }
}
