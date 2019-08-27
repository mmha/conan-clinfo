from conans import ConanFile, RunEnvironment, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "os_build", "arch_build", "compiler"

    def test(self):
        return # FIXME: Disabled for now due to ARM not being detected as a cross-build
        if tools.cross_building(self.settings):
            return
        with tools.environment_append(RunEnvironment(self).vars):
            self.run("clinfo")
