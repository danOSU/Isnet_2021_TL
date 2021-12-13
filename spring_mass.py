from manim import *

class spring_mass(Scene):

    def construct(self):

        #numberplane = NumberPlane()
        #self.add(numberplane)
        time = ValueTracker(0)
        x_max = 1
        l = 1.5
        m = 10
        k = 200
        T= 2
        w = 2 * PI/T
        exp_1 = 0.1
        exp_2 = 0.2

        p_x = -5 #desired x position
        p_y = 1.5 #desired y position
        shift_req = p_x * RIGHT + p_y * UP
        shift_req2 = (p_x-1) * RIGHT + p_y * UP

        #setting theta

        #theta = DecimalNumber().set_color(BLACK).move_to(10 * RIGHT)
        #theta.add_updater(lambda m: m.set_value((theta_max) * np.sin(w * time.get_value())))

        #self.add(theta)

        #make a line
        def get_line(x, y):
            line_here = Line(start=ORIGIN+shift_req, end=x*RIGHT+y*UP+shift_req,color=GREY)
            return line_here
        def get_line2(x, y):
            line_here = Line(start=ORIGIN+shift_req2, end=x*RIGHT+y*UP+shift_req,color=GREY)
            return line_here


        line = always_redraw(lambda: get_line(0,
                            -l + (-x_max* np.exp(-exp_1 * time.get_value()) * np.cos(w * time.get_value()))))

        line2 = always_redraw(lambda: get_line2(-1,
                            -l + (-x_max* np.exp(-exp_2 * time.get_value()) * np.cos(w * time.get_value()))))



        self.add(line)
        self.add(line2)



        #making a bob
        def get_ball(x, y):
            dot = Dot(fill_color=BLUE_E, fill_opacity=1).move_to(x*RIGHT+y*UP+shift_req).scale(1.5*l)
            return dot

        def get_ball2(x, y):
            dot = Dot(fill_color=RED, fill_opacity=1).move_to(x*RIGHT+y*UP+shift_req2).scale(1.5*l)
            return dot

        ball = always_redraw(lambda: get_ball(0,
                            -l + (-x_max* np.exp(-exp_1 * time.get_value()) * np.cos(w * time.get_value()))))

        ball2 = always_redraw(lambda: get_ball2(0,
                            -l + (-x_max* np.exp(-exp_2 * time.get_value()) * np.cos(w * time.get_value()))))

        self.add(ball)
        self.add(ball2)

        ax = Axes(x_range=[0, 20], y_range=[-1,1], axis_config={"include_tip": False}, x_length=10)
        #labels = ax.get_axis_labels(x_label="Time", y_label="Amplitude")
        ax.to_edge(LEFT,buff=3)
        #ax.to_edge(RIGHT,buff=2)

        def func(x):
            return (-x_max* np.exp(-exp_1 * x) * np.cos(w * x))
        def func2(x):
            return (-x_max* np.exp(-exp_2 * x) * np.cos(w * x))

        graph = ax.plot(func, color=BLUE)
        graph2 = ax.plot(func2, color=RED)

        initial_point = [ax.coords_to_point(time.get_value(), func(time.get_value()))]
        dot2 = Dot(point=initial_point, fill_color=BLUE_E, fill_opacity=1)
        dot3 = Dot(point=initial_point, fill_color=RED, fill_opacity=1)


        dot2.add_updater(lambda x: x.move_to(ax.c2p(time.get_value(), func(time.get_value()))))
        dot3.add_updater(lambda x: x.move_to(ax.c2p(time.get_value(), func2(time.get_value()))))

        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        #dot2_text = Text('1', font_size=23, color=WHITE).next_to(ball, DOWN)
        #dot3_text = Text('2', font_size=23, color=WHITE).next_to(ball2, DOWN)
        x_text = Text('Y', font_size=23).next_to(ball2, DOWN)


        self.add(ax, graph, graph2, dot2, dot3)
        #self.play(time.animate.set_value(x_space[minimum_index]),rate_func=linear, run_time=10*T)
        #self.wait()
        line = Line([-5, 1.5, 0], [-6, 1.5, 0])
        self.add(line)







        self.play(Transform(ball.copy(), dot2))
        self.play(Transform(ball2.copy(), dot3))

        self.play(time.animate.set_value(10* T), rate_func=linear, run_time=10*T)
