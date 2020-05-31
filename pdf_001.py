"""

Graphical unit tests

"""

from kivy.tests.common import GraphicUnitTest, UnitTestTouch

class MyTestCase(GraphicUnitTest):
    
    def test_runtouchapp(self):
        
        # non-integrated approach
        from kivy.app import runTouchApp
        from kivy.uix.button import Button
        button = Button()
        runTouchApp(button)
        
        # get your Window instance safely
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        window = EventLoop.window
        
        # your asserts
        self.assertEqual(window.children[0], button)
        self.assertEqual(
        window.children[0].height, window.height)

    class MyTestCase(GraphicUnitTest):
        
        def test_render(self):
            from kivy.uix.button import Button
            
            # with GraphicUnitTest.render() you basically do this:
            # runTouchApp(Button()) + some setup before
            button = Button()
            self.render(button)
            
            # get your Window instance safely
            from kivy.base import EventLoop
            EventLoop.ensure_window()
            window = EventLoop.window
            touch = UnitTestTouch(* [s / 2.0 for s in window.size])
            
            # bind something to test the touch with
            button.bind(on_release=lambda instance: setattr(instance, 'test_released', True))
            
            # then let's touch the Window's center
            touch.touch_down()
            touch.touch_up()
            self.assertTrue(button.test_released)

class VertexInstructionTestCase(GraphicUnitTest):

    def test_ellipse(self):
        from kivy.uix.widget import Widget
        from kivy.graphics import Ellipse, Color
        r = self.render
        
        # create a root widget
        wid = Widget()
        
        # put some graphics instruction on it
        with wid.canvas:
            Color(1, 1, 1)
            self.e = Ellipse(pos=(100, 100), size=(200, 100))
            
        # render, and capture it directly
        r(wid)
        
        # as alternative, you can capture in 2 frames:
        r(wid, 2)
        
        # or in 10 frames
        r(wid, 10)

if __name__ == '__main__':
    import unittest
    unittest.main()
