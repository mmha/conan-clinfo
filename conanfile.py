from conans import ConanFile, CMake, tools
import os


class ClinfoConan(ConanFile):
    name = "clinfo"
    version = "2.2.18.04.06"
    settings = "os", "arch"
    description = "Print all known information about all available OpenCL platforms and devices in the system"
    topics = ("clinfo", "khronos", "opencl", "gpu")
    url = "https://github.com/mmha/conan-clinfo"
    homepage = "https://github.com/Oblomov/clinfo"
    author = "Morris Hafner <hafnermorris@gmail.com>"
    license = "CC-0"
    exports = ["LICENSE.md", "CMakeLists.txt"]
    generators = "cmake"

    settings = "arch", "os", "compiler"

    requires = "khronos-opencl-icd-loader/[>=20190507]@bincrafters/stable"

    default_options = {
        "khronos-opencl-icd-loader:shared": True
    }

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        sha256 = "f77021a57b3afcdebc73107e2254b95780026a9df9aa4f8db6aff11c03f0ec6c"
        source_url = "https://github.com/Oblomov/clinfo"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version

        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst=f"licenses/{self.name}", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        del self.info.settings.compiler

    def package_info(self):
        bindir = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH environment variable: {}".format(bindir))
        self.env_info.PATH.append(bindir)
