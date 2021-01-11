from talon import ctrl, ui, Module, Context, actions, clip, app

ctx = Context()
mod = Module()

mod.apps.emacs = "app.name: Emacs"

ctx.matches = r"""
app: emacs
"""


@ctx.action_class("user")
class user_actions:
    pass
