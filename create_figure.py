from figure_class import flat_figures, volume_figures

figures_types = {"2D": "flat",
                 "3D": 'volume',
                 }


class CreateFigure:
    object = None
    fig_type = ""
    figure = ""
    params = []
    operation = ""

    @staticmethod
    def convert_type(t):
        return figures_types[t]

    @classmethod
    def set_figure(cls, item):
        cls.figure = item

    @classmethod
    def get_figure(cls):
        return cls.figure

    @classmethod
    def set_type(cls, item):
        cls.fig_type = item

    @classmethod
    def get_type(cls):
        return cls.fig_type

    @classmethod
    def set_operation(cls, item):
        cls.operation = item

    @classmethod
    def get_operation(cls):
        return cls.operation

    @classmethod
    def set_params(cls, arg_list):
        cls.params = arg_list

    @classmethod
    def get_params(cls):
        return cls.params

    @classmethod
    def get_result(cls):
        if cls.convert_type(cls.fig_type) == "flat":
            cls.object = flat_figures[cls.figure](*cls.params)
        elif cls.convert_type(cls.fig_type) == "volume":
            cls.object = volume_figures[cls.figure](*cls.params)
        if cls.operation == "S - площадь фигуры":
            return cls.object.area
        elif cls.operation == "V - обьем фигуры":
            return cls.object.volume
