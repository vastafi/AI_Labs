from production import IF, AND, THEN, OR

TOURIST_RULES = (
    IF(AND('(?x) has strong and muscular body',       # H1
           '(?x) has big and strong teeth',
           '(?x) has long face',
           '(?x) has prominent sagittal ridge'),
       THEN('(?x) is from Paleolithic')),

    IF(OR('(?x) dressed in animal skins',             # H2
          '(?x) dressed in woolen fabrics'),
       THEN('(?x) is from Mesolithic')),

    IF(AND('(?x) has tattoos',                         # H3
           '(?x) has forehead is vertical and slightly inclined'
           '(?x) has loses weight from'),
       THEN('(?x) is from Mesolithic')),

    IF(AND('(?x) has small teeth',                     # H4
           '(?x) has rounded skull',
           '(?x) has flat face',
           '(?x) has slender body',
           '(?x) has loses weight from'),
        THEN('(?x) is from Neolithic')),

    IF(AND('(?x) is from Paleolithic',                  # H8
           '(?x) has a limited social behavior'),
       THEN('(?x) is Homo Erectus')),

    IF(OR('(?x) has tool manufacturing occupation',      # H9
          '(?x) has interested in seeking cultural experiences'),
        THEN('(?x) is Homo Erectus')),

    IF(AND('(?x) has articulated language',              # H11
           '(?x) is from Paleolithic'),
        THEN('(?x) is Homo Sapiens')),

    IF(AND('(?x) has robust stature',                    # H12
           '(?x) is from Mesolithic'),
        THEN('(?x) is Homo Sapiens')),

    IF(AND('(?x) has climbing behavior',                 # H13
           '(?x) is from Neolithic'),
       THEN('(?x) is Homo Habilis')),

    IF(AND('(?x) is from Neolithic',                     # H14
           '(?x) has adaptation to cold climate'),
       THEN('(?x) is Neanderthal')),

    IF(AND('(?x) is from Neolithic',                     # H15
           '(?x) has capable of fine manipulation'),
       THEN('(?x) is Homo Naledi')),
)

TOURIST_DATA = (
    # 'tourist has strong and muscular body',
    # 'tourist has big and strong teeth',
    # 'tourist has long face',
    # 'tourist has prominent sagittal ridge',
    # 'tourist dressed in animal skins',
    # 'tourist dressed in woolen fabrics',
    # 'tourist has tattoos',
    # 'tourist is forehead is vertical and slightly inclined',
    # 'tourist loses weight from',
    # 'tourist has small teeth',
    # 'tourist has rounded skull',
    # 'tourist has flat face',
    # 'tourist has slender body',
    # 'tourist loses weight from',
    # 'tourist is from Paleolithic',
    # 'tourist has a limited social behavior',
    # 'tourist has tool manufacturing occupation',
    # 'tourist has interested in seeking cultural experiences',
    # 'tourist has articulated language',
    # 'tourist has robust stature',
    # 'tourist is from Mesolithic',
    # 'tourist has climbing behavior',
    # 'tourist is from Neolithic',
    # 'tourist has adaptation to cold climate',
    # 'tourist has partially adapted for climbing',
    'tourist has capable of fine manipulation',
    'tourist is from Neolithic',
    # 'tourist has interested in community events',
)
