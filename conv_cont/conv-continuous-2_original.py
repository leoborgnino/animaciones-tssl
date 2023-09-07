#!/usr/bin/env python

from manimlib.imports import *
import numpy as np

TIME_SCALE = 0.5

class Conv(GraphScene):
    CONFIG = {
        "y_max" : 30,
        "y_min" : -10,
        "x_max" : 10,
        "x_min" : -10,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "graph_origin" : [0, -2.5, 0],
        "y_axis_label": None,
        "x_axis_label": None,
        "x_axis_width": 20,
        "y_axis_height": 40,
    }

    # Funcion que crea la pantalla principal
    def titulo_credits (self, titulo, subtitulo, creditos):
        # Introduccion
        # Titulo
        title = TextMobject(titulo)
        title.scale(2)
        # Subtitulo
        subtitle = TextMobject(subtitulo)
        subtitle.scale(1)
        subtitle.move_to([0, -1.0, 0])
        # Creditos
        creators = TextMobject(creditos)
        creators.scale(0.5)
        creators.move_to([4.5, -3.8, 0])
        self.play(Write(title), run_time=TIME_SCALE*1.2)
        self.play(Write(subtitle), run_time=TIME_SCALE*0.5)
        self.wait(TIME_SCALE*1)
        self.play(Write(creators), run_time=TIME_SCALE*0.7)
        self.wait(TIME_SCALE*1)
        self.play(FadeOut(title))
        self.play(FadeOut(subtitle))
        self.wait(TIME_SCALE*2)

    def etiquetas_eje_t(self, y0):
        # Etiqueta del tiempo
        label_t = TextMobject(" t ")
        label_t.move_to([6.5, y0 - 0.4 , 0])
        label_t.set_color(RED)
        # Numeros del eje de tiempos
        range_t = [-5,5]
        for i in np.linspace(range_t[0],range_t[1],(range_t[1]-range_t[0])+1):
            label_0 = TextMobject(str(int(i)))
            label_0.move_to([i+0.1, y0 - 0.3 , 0])
            label_0.set_color(RED)
            label_0.scale(0.5)
            self.play(Write(label_0),run_time=TIME_SCALE*0)

        range_x = [-1,2]
        for i in np.linspace(range_x[0],range_x[1],(range_x[1]-range_x[0])+1):
            if(i==0):
                pass
            else:
                label_0 = TextMobject(str(int(i)))
                label_0.move_to([0.1+0.2, i + y0 -0.2 , 0])
                label_0.set_color(RED)
                label_0.scale(0.5)
                self.play(Write(label_0),run_time=TIME_SCALE*0)

        self.play(Write(label_t), run_time=TIME_SCALE*1)
        self.wait(TIME_SCALE*1)

        return label_t

    def conv_definition(self):
        conv_text = TextMobject("Convolución Contínua:")
        conv_text.move_to([-4, 3, 0])
        self.play(Write(conv_text))
        self.wait(TIME_SCALE*0.2)
        #
        conv_formula = TextMobject(
            "{\\small $y(t)=$}",
            "{\\small $\\ x(t)*h(t)=$}",
            "{\\small $\int\limits_{-\infty}^{\infty}x(\\tau)h(t-\\tau)d\\tau$}"
        )
        conv_formula.scale(0.85)
        conv_formula.move_to([-3.5, 2.2, 0])
        self.play(Write(conv_formula))
        self.wait(TIME_SCALE*1)

        return conv_formula, conv_text

    def draw_x_t(self,y0):
        # Grupo de segmentos
        xt = VGroup()
        # Cada segmento del grupo
        x1 = Line([-8, y0, 0], [0, y0, 0])
        x1.set_color(GREEN)
        x2 = Line([0, y0, 0], [0, 1 + y0, 0])
        x2.set_color(GREEN)
        x3 = Line([0, 1 + y0, 0], [1, 1 + y0, 0])
        x3.set_color(GREEN)
        x4 = Line([1, 1 + y0, 0], [1, y0, 0])
        x4.set_color(GREEN)
        x5 = Line([1, y0, 0], [8, y0, 0])
        x5.set_color(GREEN)
        #
        xt.add(x1, x2, x3, x4, x5)
        self.play(ShowCreation(x1, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(x2, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(x3, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(x4, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(x5, run_time=TIME_SCALE*0.5))
        self.wait(TIME_SCALE*1)
        # TExto de la señal
        xt_text = TextMobject("""
            $$x(t)=u(t)-u(t-1)$$
        """)
        xt_text.set_color(GREEN)
        xt_text.move_to([3.5, 3, 0])
        self.play(Write(xt_text))
        self.wait(TIME_SCALE*1)

        return xt, xt_text

    def draw_h_t(self, y0):
        ht = VGroup()
        h1 = Line([-8, y0, 0], [-3, y0, 0])
        h1.set_color(BLUE)
        h2 = Line([-3, y0, 0], [-3, 2 + y0, 0])
        h2.set_color(BLUE)
        h3 = Line([-3, 2 + y0, 0], [-1, 2 + y0, 0])
        h3.set_color(BLUE)
        h4 = Line([-1, 2 + y0, 0], [-1, y0, 0])
        h4.set_color(BLUE)
        h5 = Line([-1, y0, 0], [8, y0, 0])
        h5.set_color(BLUE)
        
        ht.add(h1,h2,h3,h4,h5)
        self.play(ShowCreation(h1, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(h2, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(h3, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(h4, run_time=TIME_SCALE*0.5))
        self.play(ShowCreation(h5, run_time=TIME_SCALE*0.5))
        self.wait(TIME_SCALE*1)
        
        ht_text = TextMobject("""
            $$h(t)=2 [u(t+3)-u(t+1)]$$
        """)
        ht_text.set_color(BLUE)
        ht_text.move_to([3.5, 2.3, 0])
        self.play(Write(ht_text))
        self.wait(TIME_SCALE*1)

        return ht, ht_text

    def move_conv_formula(self,conv_formula, conv_text):
        ## removing convolution text and putting the formula in a corner
        corner_conv_formula = TextMobject(
            "{\\small $y(t)=$}",
            "{\\small $\int\limits_{-\infty}^{\infty}x(\\tau)h(t-\\tau)d\\tau$}"
        )
        offset_top = 0.3
        corner_conv_formula.move_to([-3.5, 3+offset_top, 0])
        corner_conv_formula.scale(0.8)
        self.play(
            FadeOut(conv_text),
            FadeOut(conv_formula[1]),
            ReplacementTransform(conv_formula[0], corner_conv_formula[0]),
            ReplacementTransform(conv_formula[2], corner_conv_formula[1])
        )
        self.wait(TIME_SCALE*0.2)

        convolution_rect = Polygon([-5.45, 2.55+offset_top, 0], [-1.6, 2.55+offset_top, 0],
                              [-1.6, 3.45+offset_top, 0], [-5.45, 3.45+offset_top, 0])
        convolution_rect.set_color(WHITE)
        convolution_rect.scale(1.1)
        self.play(Write(convolution_rect))
        self.wait(TIME_SCALE*1)

        return corner_conv_formula, convolution_rect

    def change_t_to_tau (self, y0, xt_text, ht_text, label_t):
        t_to_tau = TextMobject("""$$Paso \\ 1: \\; t \\rightarrow \\tau$$""")
        t_to_tau.scale(0.9)
        t_to_tau.move_to([-3.5, 2.1, 0])
        self.play(Write(t_to_tau))
        self.wait(TIME_SCALE*1)
        #
        xtau_text = TextMobject("""
            $$x(\\tau)= u(\\tau)-u(\\tau-1)$$
        """)
        xtau_text.set_color(GREEN)
        xtau_text.move_to([3.5, 3, 0])
        
        htau_text = TextMobject("""
            $$h(\\tau)=2 [u(\\tau+3)-u(\\tau+1)]$$
        """)
        htau_text.set_color(BLUE)
        htau_text.move_to([3.5, 2.3, 0])
        
        label_tau = TextMobject("""$$\\tau$$""")
        label_tau.move_to([6.5, 0.4 + y0, 0])
        label_tau.set_color(RED)
        
        self.play(
            ReplacementTransform(xt_text, xtau_text),
            ReplacementTransform(ht_text, htau_text),
            Transform(label_t, label_tau)
        )
        self.wait(TIME_SCALE*1)
        self.play(FadeOut(t_to_tau))       

        return xtau_text, htau_text, label_tau

    def ht_reflect(self,y0,ht, htau_text):
        htau_to_hmtau = TextMobject("""$Paso \\ 2: \\; h(\\tau) \\rightarrow h(-\\tau)$""")
        htau_to_hmtau.scale(0.9)
        htau_to_hmtau.move_to([-3.6, 2.1, 0])
        self.play(Write(htau_to_hmtau))
        self.wait(TIME_SCALE*1)
        
        hmtau_text = TextMobject("""
            $$h(-\\tau)=2 [u(-\\tau+3)-u(-\\tau+1)] $$
        """)
        hmtau_text.set_color(BLUE)
        hmtau_text.move_to([3.5, 2.3, 0])
        hmtau_text.scale(0.95)
        
        hmtau = VGroup()
        hm1 = Line([-8, y0, 0], [1, y0, 0])
        hm1.set_color(BLUE)
        hm2 = Line([1, y0, 0], [1, 2 + y0, 0])
        hm2.set_color(BLUE)
        hm3 = Line([1, 2 + y0, 0], [3, 2 + y0, 0])
        hm3.set_color(BLUE)
        hm4 = Line([3, 2 + y0, 0], [3, y0, 0])
        hm4.set_color(BLUE)
        hm5 = Line([3, y0, 0], [8, y0, 0])
        hm5.set_color(BLUE)
        
        hmtau.add(hm1, hm2, hm3, hm4, hm5)
        self.play(FadeOut(ht))
        self.wait(TIME_SCALE*0.5)
        self.play(Write(hmtau))
        self.play(ReplacementTransform(htau_text, hmtau_text))
        self.wait(TIME_SCALE*1)
        self.play(FadeOut(htau_to_hmtau))

        return hmtau, hmtau_text

    def moving_window_intro(self,y0,hmtau_text):
        wind_and_multiply = TextMobject("Paso 3 \\ : Señal Móvil")
        wind_and_multiply.scale(0.9)
        wind_and_multiply.move_to([-3.5, 3+0.3, 0])        
        self.play(Write(wind_and_multiply))
        self.wait(TIME_SCALE*0.5)
        
        htmtau_text = TextMobject("""
            $$h(t-\\tau)=2 [u(t-\\tau+1) - u(t-\\tau+3)]$$
        """)
        htmtau_text.set_color(BLUE)
        htmtau_text.move_to([3.5, 2.3, 0])
        htmtau_text.scale(0.75)
        self.play(ReplacementTransform(hmtau_text, htmtau_text))
        self.wait(TIME_SCALE*0.5)
        # Limites señal movil
        inf_limit_text = TextMobject("""
            $$t+1$$
        """)
        inf_limit_text.set_color(BLUE)
        inf_limit_text.move_to([1, y0-0.6, 0])
        inf_limit_text.scale(0.6)
        self.play(Write(inf_limit_text))
                  
        sup_limit_text = TextMobject("""
            $$t+3$$
        """)
        sup_limit_text.set_color(BLUE)
        sup_limit_text.move_to([3, y0-0.6, 0])
        sup_limit_text.scale(0.6)
        self.play(Write(sup_limit_text))
        
        # Instrucciones
        guide_1 = TextMobject("""
            para todo t: tomar la integral de 
        """)
        guide_1.scale(0.75)
        guide_1.move_to([-3.8, 0.6, 0])
        
        guide_2 = TextMobject("""
            la multiplicación de las señales,
        """)
        guide_2.scale(0.75)
        guide_2.move_to([-3.5, 0.25, 0])
        
        guide_3 = TextMobject("""
            desde $-\\infty$ a $+\\infty$. 
        """)
        guide_3.scale(0.75)
        guide_3.move_to([-4.7, -0.1, 0])

        self.play(Write(guide_1))
        self.play(Write(guide_2))
        self.play(Write(guide_3))
        self.wait(TIME_SCALE*2)
        #
        self.play(FadeOut(guide_1), FadeOut(guide_2), FadeOut(guide_3))

        return htmtau_text, inf_limit_text, sup_limit_text

        
    # "Main"
    def construct(self):

        # Pantalla Inicial
        self.titulo_credits("Convolución Contínua","Ejemplo 2","Ing Leandro Borgnino TSSL UNC 2023")

        # Creacion Pantalla principal
        # Ejes del proceso de convolucion
        self.setup_axes()
        y0 = -2.5
        label_t = self.etiquetas_eje_t(y0)
        
        # Definicion Convolucion Continua
        conv_formula, conv_text = self.conv_definition()

        # Dibujado funcion x(t)
        xt, xt_text = self.draw_x_t(y0)

        # Dibujado funcion h(t)
        ht, ht_text = self.draw_h_t(y0)

        # Mover la formula de convolucion
        corner_conv_formula, convolution_rect = self.move_conv_formula(conv_formula, conv_text)

        ## Paso 1: t -> tau
        xtau_text, htau_text, label_tau = self.change_t_to_tau(y0, xt_text, ht_text, label_t)
        
        ## Paso 2: h(tau) -> h(-tau+t)

        hmtau, hmtau_text = self.ht_reflect(y0, ht, htau_text)
        
        ## Paso 3: Ventana Deslizante

        # Textos
        self.play(FadeOut(corner_conv_formula), FadeOut(convolution_rect))

        htmtau_text, inf_limit_text, sup_limit_text = self.moving_window_intro(y0,hmtau_text)
        
        
        # Mover Htmtau Deslizante
        # necesita y0, hmtau, los limites
        window = VGroup()
        window.add(hmtau)
        offset = -8
        pos_hh = 3

        # Arrow
        arr = Arrow([pos_hh, y0 - 0.8, 0], [pos_hh, y0 + 0.2, 0])
        self.play(Write(arr))
        window.add(arr)
        
        # Se mueve la ventana a la izquierda offset
        self.play(
            hmtau.shift, [offset, 0, 0],
            inf_limit_text.shift, [offset, 0, 0],
            sup_limit_text.shift, [offset, 0, 0],
            arr.shift, [offset, 0, 0],
            run_time=TIME_SCALE*2
        )
        self.wait(TIME_SCALE*1)

        # Movimiento de t
        # ValueTracker for t
        t_label = TexMobject("t=", )
        t_label.scale(0.8)
        t_label.move_to([offset + pos_hh - 0.8, -3.4, 0])
        
        def t_updater(obj):
            val = t_value.get_value()
            obj.set_value(val)
            obj.move_to([val + pos_hh, -3.4, 0])
        
        t_value = ValueTracker(offset)
        t_text = DecimalNumber(offset)
        t_text.scale(0.8)
        t_text.add_updater(t_updater)
        t_text.move_to([offset + pos_hh, -3.4, 0])
        #
        #
        self.play(Write(t_text), Write(t_label))
        self.wait(TIME_SCALE*1)
        #
        window.add(t_label, sup_limit_text, inf_limit_text)
        #
        #
        ## Linea del Resultado de la Convolución
        yz = 0.5
        number_line = NumberLine(y_min=-8, y_max=8, unit_size=1, numbers_with_elongated_ticks=[])
        number_line.set_stroke(width=1)
        number_line.move_to([0, yz, 0])
        self.play(Write(number_line))
        #
        y_text = TextMobject("y(t)")
        y_text.set_color(ORANGE)
        y_text.scale(0.8)
        y_text.move_to([-5.5, -0.1+1.0, 0])
        self.play(Write(y_text))
        self.wait(TIME_SCALE*1)

        range_t = [-5,5]
        for i in np.linspace(range_t[0],range_t[1],(range_t[1]-range_t[0])+1):
            label_0 = TextMobject(str(int(i)))
            label_0.move_to([i+0.1, yz - 0.3 , 0])
            label_0.set_color(ORANGE)
            label_0.scale(0.5)
            self.play(Write(label_0),run_time=0)

        range_x = [0,3]
        for i in np.linspace(range_x[0],range_x[1],(range_x[1]-range_x[0])+1):
            if(i==0):
                pass
            else:
                label_0 = TextMobject(str(int(i)))
                label_0.move_to([0.1+0.2, i + yz, 0])
                label_0.set_color(ORANGE)
                label_0.scale(0.5)
                self.play(Write(label_0),run_time=TIME_SCALE*0)
        #
        #
        ## Resultado de la convolucion
        y1 = Line([-8, yz, 0], [-3, yz, 0])
        y1.set_color(ORANGE)
        y2 = Line([-3, 0 + yz, 0], [-2, 2 + yz, 0])
        y2.set_color(ORANGE)
        y3 = Line([-2, 2 + yz, 0], [-1, 2 + yz, 0])
        y3.set_color(ORANGE)
        y4 = Line([-1, 2 + yz, 0], [0,  0 + yz, 0])
        y4.set_color(ORANGE)
        y5 = Line([0, 0+yz, 0], [3, 0+yz, 0])
        y5.set_color(ORANGE)
        #
        #
        ## dots 1
        #dots_1 = TextMobject("...")
        #dots_1.move_to([-4.32, -0.5, 0])
        #dots_1.scale(1.4)
        #dots_1.set_color(ORANGE)
        #self.play(Write(dots_1))
        #
        # Primer intervalo
        self.play(FadeOut(htmtau_text),FadeOut(xtau_text))

        first_interval_title = TextMobject("""
            Intervalo I.
        """)
        first_interval_title.set_color(ORANGE)
        first_interval_title.move_to([3.5, 3.5, 0])
        first_interval_title.scale(0.8)       

        first_interval_t = TextMobject("""
            $$ t \leq -3$$
        """)
        first_interval_t.set_color(ORANGE)
        first_interval_t.move_to([3.5, 3, 0])
        first_interval_t.scale(0.8)       

        first_interval_y = TextMobject("""
            $$ y(t) = 0$$
        """)
        first_interval_y.set_color(ORANGE)
        first_interval_y.move_to([3.5, 2.3, 0])
        first_interval_y.scale(0.8)

        self.play(Write(first_interval_t), Write(first_interval_y), Write(first_interval_title))
        
        ## Se mueve la ventana un offset por un runtime
        self.play(
            window.shift, [5, 0, 0],
            sup_limit_text.shift, [5, 0, 0],
            inf_limit_text.shift, [5, 0, 0],
            t_value.set_value, -3,
            ShowCreation(y1),
            rate_func=linear,
            run_time=TIME_SCALE*4
        )
        #
        #
        ## Intersección del área
        one = self.get_graph(lambda x: 2, x_min=0, x_max=1)
        area = self.color_area(one, 0, 1)
        area.set_color(YELLOW)
        #area.set_z_index(0)
        #
        self.play(FadeOut(first_interval_t),FadeOut(first_interval_y),FadeOut(first_interval_title))

        second_interval_title = TextMobject("""
            Intervalo II.
        """)
        second_interval_title.set_color(ORANGE)
        second_interval_title.move_to([3.5, 3.5, 0])
        second_interval_title.scale(0.8)       

        second_interval_t = TextMobject("""
            $$ -3 < t \leq -2$$
        """)
        second_interval_t.set_color(ORANGE)
        second_interval_t.move_to([3.5, 3, 0])
        second_interval_t.scale(0.8)       

        second_interval_y = TextMobject("""
            $$ y(t) = \int_{0}^{t+3} 2 d \\tau = 2t+6$$
        """)
        second_interval_y.set_color(ORANGE)
        second_interval_y.move_to([3.5, 2.0, 0])
        second_interval_y.scale(0.8)
        
        self.play(Write(second_interval_t), Write(second_interval_y), Write(second_interval_title))

        self.play(
            window.shift, [1, 0, 0],
            t_value.set_value, -2,
            ShowCreation(area),
            ShowCreation(y2),
            rate_func=linear,
            run_time=TIME_SCALE*4
        )
        
        self.play(FadeOut(second_interval_t),FadeOut(second_interval_y),FadeOut(second_interval_title))
        
        third_interval_title = TextMobject("""
            Intervalo III.
        """)
        third_interval_title.set_color(ORANGE)
        third_interval_title.move_to([3.5, 3.5, 0])
        third_interval_title.scale(0.8)       

        third_interval_t = TextMobject("""
            $$ -2 < t \leq -1$$
        """)
        third_interval_t.set_color(ORANGE)
        third_interval_t.move_to([3.5, 3, 0])
        third_interval_t.scale(0.8)       

        third_interval_y = TextMobject("""
            $$ y(t) = \int_{0}^{1} 2 d \\tau = 2 $$
        """)
        third_interval_y.set_color(ORANGE)
        third_interval_y.move_to([3.5, 2.0, 0])
        third_interval_y.scale(0.8)
        
        self.play(Write(third_interval_t), Write(third_interval_y), Write(third_interval_title))

        self.play(
            window.shift, [1, 0, 0],
            t_value.set_value, -1,
            ShowCreation(y3),
            rate_func=linear,
            run_time=TIME_SCALE*4
        )

        self.play(FadeOut(third_interval_t),FadeOut(third_interval_y),FadeOut(third_interval_title))

        fourth_interval_title = TextMobject("""
            Intervalo IV.
        """)
        fourth_interval_title.set_color(ORANGE)
        fourth_interval_title.move_to([3.5, 3.5, 0])
        fourth_interval_title.scale(0.8)       

        fourth_interval_t = TextMobject("""
            $$ -1 \leq t < 0 $$
        """)
        fourth_interval_t.set_color(ORANGE)
        fourth_interval_t.move_to([3.5, 3, 0])
        fourth_interval_t.scale(0.8)       

        fourth_interval_y = TextMobject("""
            $$ y(t) = \int_{t+1}^1 2 d \\tau = -2t $$
        """)
        fourth_interval_y.set_color(ORANGE)
        fourth_interval_y.move_to([3.5, 2.0, 0])
        fourth_interval_y.scale(0.8)
        
        self.play(Write(fourth_interval_t), Write(fourth_interval_y), Write(fourth_interval_title))
        #
        #self.play(FadeOut(area))
        one = self.get_graph(lambda x: 2, x_min=0, x_max=1)
        area2 = self.color_area(one, 0, 1, opacity=2.0)
        area2.set_color(BLACK)
        area2.set_opacity(1)
        #area2.set_z_index(1)
        
        #
        self.play(
            window.shift, [1, 0, 0],
            t_value.set_value, 0,
            ShowCreation(y4),
            ShowCreation(area2),
            rate_func=linear,
            run_time=TIME_SCALE*4
        )

        self.play(FadeOut(fourth_interval_t),FadeOut(fourth_interval_y),FadeOut(fourth_interval_title))

        fifth_interval_title = TextMobject("""
            Intervalo V.
        """)
        fifth_interval_title.set_color(ORANGE)
        fifth_interval_title.move_to([3.5, 3.5, 0])
        fifth_interval_title.scale(0.8)       

        fifth_interval_t = TextMobject("""
            $$ t \geq 0 $$
        """)
        fifth_interval_t.set_color(ORANGE)
        fifth_interval_t.move_to([3.5, 3, 0])
        fifth_interval_t.scale(0.8)       

        fifth_interval_y = TextMobject("""
            $$ y(t) = 0 $$
        """)
        fifth_interval_y.set_color(ORANGE)
        fifth_interval_y.move_to([3.5, 2.0, 0])
        fifth_interval_y.scale(0.8)
        
        self.play(Write(fifth_interval_t), Write(fifth_interval_y), Write(fifth_interval_title))

        #
        self.play(
            window.shift, [3, 0, 0],
            t_value.set_value, 3,
            ShowCreation(y5),
            rate_func=linear,
            run_time=TIME_SCALE*4
        )

        #
        self.wait(TIME_SCALE*5)

    def setup_axes(self):
        GraphScene.setup_axes(self)

        # width of edges
        self.x_axis.set_stroke(width=1)
        self.y_axis.set_stroke(width=1)

        # color of edges
        self.x_axis.set_color(RED)
        self.y_axis.set_color(RED)
        self.play(
            *[Write(objeto)
            for objeto in [self.y_axis, self.x_axis]],
            run_time=2
    )

    def color_area(self, graph, t_min, t_max, opacity = 0.5):
        numerator = max(t_max - t_min, 0.0001)
        dx = float(numerator) / 1000
        return self.get_riemann_rectangles(
            graph,
            x_min=t_min,
            x_max=t_max,
            dx=dx,
            stroke_width=0,
        ).set_fill(opacity=opacity)
