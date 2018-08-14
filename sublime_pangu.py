import sublime
import sublime_plugin
from .pangu import spacing_text


class PanguCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cur_text = self.view.substr(sublime.Region(0, self.view.size()))
        self.view.replace(edit, sublime.Region(0, self.view.size()),
                          spacing_text(cur_text))
