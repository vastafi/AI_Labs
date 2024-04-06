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
    'John has strong and muscular body',
    'John has big and strong teeth',
    'John has long face',
    'John has prominent sagittal ridge',
    'Alice dressed in animal skins',
    'Bob dressed in woolen fabrics',
    'Carol has tattoos',
    'Carol is forehead is vertical and slightly inclined',
    'Carol loses weight from',
    'Dave has small teeth',
    'Dave has rounded skull',
    'Dave has flat face',
    'Dave has slender body',
    'Eve loses weight from',
    'Frank is from Paleolithic',
    'Frank has a limited social behavior',
    'George has tool manufacturing occupation',
    'Helen has interested in seeking cultural experiences',
    'Ian has articulated language',
    'Jack has robust stature',
    'Jack is from Mesolithic',
    'Lucy has climbing behavior',
    'Lucy is from Neolithic',
    'Mia has adaptation to cold climate',
    'Nate has partially adapted for climbing',
    'Olivia has capable of fine manipulation',
    'Olivia is from Neolithic',
    'Peter has interested in community events',
)
