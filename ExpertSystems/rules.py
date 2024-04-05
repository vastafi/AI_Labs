from production import IF, AND, THEN, OR

TOURIST_RULES = (

    IF(AND('(?x) has strong and muscular body',   # H1
           '(?x) has big and strong teeth',
           '(?x) has long face',
           '(?x) has prominent sagittal ridge'),
       THEN('(?x) is from Paleolithic')),

    IF(OR('(?x) dressed in animal skins',         # H2
          '(?x) dressed in woolen fabrics'),
       THEN('(?x) might be from Paleolithic or Neolithic')),

    IF(AND('(?x) has tattoos',                    # H3
           '(?x) has forehead is vertical and slightly inclined'
           '(?x) has loses weight from'),
       THEN('(?x) is from Mesolithic')),

    IF(AND('(?x) has small teeth',                # H4
           '(?x) has rounded skull',
           '(?x) has flat face',
           '(?x) has slender body',
           '(?x) has loses weight from'),
        THEN('(?x) is from Neolithic')),

    IF(AND('(?x) loses weight from'),                   # H5
        THEN('(?x) might be from Paleolithic to Mesolithic')),

    IF(AND('(?x) dressed in animal skins'),              # H6
       THEN('(?x) might be from Paleolithic to Mesolithic')),

    IF(AND('(?x) dressed in woolen fabrics'),            # H7
       THEN('(?x) might be from Neolithic to Mesolithic')),

    IF(AND('(?x) is from Paleolithic',            # H8
       '(?x) has a limited social behavior'),
       THEN('(?x) is Homo Erectus')),

    IF(OR('(?x) has tool manufacturing occupation',      # H9
          '(?x) has interested in seeking cultural experiences'),
        THEN('(?x) is Homo Erectus')),

    IF(OR(AND('(?x) is from Paleolithic',          # H10
              '(?x) has interested in seeking cultural experiences'),
          '(?x) has a limited social behavior',
          '(?x) has a limited social behavior'),
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

    IF(OR(AND('(?x) is from Neolithic',            # H14
              '(?x) has adaptation to cold climate'),
          '(?x) has partially adapted for climbing'),
       THEN('(?x) is Neanderthal')),

    IF(OR(AND('(?x) is from Neolithic',            # H15
              '(?x) has capable of fine manipulation'),
          '(?x) has interested in community events'),
       THEN('(?x) is Homo Naledi')),
)

TOURIST_DATA = (
    'John has strong and muscular body',                   # H1
    'John has big and strong teeth',
    'John has long face',
    'John has prominent sagittal ridge',
    'Alice dressed in animal skins',                       # H2 și H6
    'Bob dressed in woolen fabrics',                       # H2 și H7
    'Carol has tattoos',                                   # H3
    'Carol is forehead is vertical and slightly inclined',
    'Carol loses weight from',
    'Dave has small teeth',                                 # H4
    'Dave has rounded skull',
    'Dave has flat face',
    'Dave has slender body',
    'Eve loses weight from',                                 # H5
    'Frank is from Paleolithic',                             # H8, H10 și H11
    'Frank has a limited social behavior',
    'George has tool manufacturing occupation',              # H9
    'Helen has interested in seeking cultural experiences',  # H10
    'Ian has articulated language',                          # H11
    'Jack has robust stature',                               # H12
    'Jack is from Mesolithic',
    'Lucy has climbing behavior',                            # H13
    'Lucy is from Neolithic',
    'Mia has adaptation to cold climate',                    # H14
    'Nate has partially adapted for climbing',               # H14
    'Olivia has capable of fine manipulation',               # H15
    'Olivia is from Neolithic',
    'Peter has interested in community events',              # H15
)
