from django.db import models


class StateChoices(models.TextChoices):
    ALBERTA = 'Alberta'
    BRITISH_COLUMBIA = 'British Columbia'
    MANITOBA = 'Manitoba'
    NEW_BRUNSWICK = 'New Brunswick'
    NEWFOUNDLAND_AND_LABRADOR = 'Newfoundland and Labrador'
    NOVA_SCOTIA = 'Nova Scotia'
    ONTARIO = 'Ontario'
    PRINCE_EDWARD_ISLAND = 'Prince Edward Island'
    QUEBEC = 'Quebec'
    SASKATCHEWAN = 'Saskatchewan'


class CitiesChoices(models.TextChoices):
    VANCOUVER = 'Vancouver'
    VICTORIA = 'Victoria'
    SURREY = 'Surrey'
    BURNABY = 'Burnaby'
    RICHMOND = 'Richmond'
    KELOWNA = 'Kelowna'
    KAMLOOPS = 'Kamloops'
    NANAIMO = 'Nanaimo'
    PRINCE_GEORGE = 'Prince George'
    NEW_WESTMINSTER = 'New Westminster'
    ABBOTSFORD = 'Abbotsford'
    COQUITLAM = 'Coquitlam'
    CHILLIWACK = 'Chilliwack'
    LANGLEY = 'Langley'
    MAPLE_RIDGE = 'Maple Ridge'
    PORT_COQUITLAM = 'Port Coquitlam'
    VERNON = 'Vernon'
    SAANICH = 'Saanich'
    DELTA = 'Delta'
    WHITE_ROCK = 'White Rock'
    WEST_VANCOUVER = 'West Vancouver'
    PENTICTON = 'Penticton'
    CAMPBELL_RIVER = 'Campbell River'
    NORTH_VANCOUVER = 'North Vancouver'
    COURTENAY = 'Courtenay'
    PORT_MOODY = 'Port Moody'
    FORT_ST_JOHN = 'Fort St. John'
    SALMON_ARM = 'Salmon Arm'
    DUNCAN = 'Duncan'
    PARKSVILLE = 'Parksville'
    SQUAMISH = 'Squamish'
    MERRITT = 'Merritt'
    TERRACE = 'Terrace'
    ROSSLAND = 'Rossland'
