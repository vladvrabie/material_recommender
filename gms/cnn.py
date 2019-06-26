import random


def hardcoded_predict(material_data):
    folder1 = ('C:\\Users\\vladv\\Desktop\\test\\h200\\', 'b_')
    folder2 = ('C:\\Users\\vladv\\Desktop\\test\\0_14_12__0\\', 'a_a_')
    # folder3 = ('C:\\Users\\vladv\\Desktop\\test\\18_6_40__0\\', 'b_')
    sel = random.sample((folder1, folder2), 1)[0]
    material_data.id = sel[1]
    material_data.load_from_folder(
        sel[0],
        frames_count=25,
        prefix=sel[1],
        extension='.png'
    )


def predict(shader_values):
    # TODO: implement cnn predict
    pass
