package(default_visibility = ["//visibility:public"])

licenses(["notice"])

load(
    "@io_bazel_rules_go//go:def.bzl",
    "go_library",
    "go_test",
)

go_library(
    name = "go_default_library",
    srcs = ["webhook.go"],
    tags = ["automanaged"],
    deps = [
        "//pkg/apis/authentication/install:go_default_library",
        "//pkg/apis/authentication/v1beta1:go_default_library",
        "//pkg/client/clientset_generated/clientset/typed/authentication/v1beta1:go_default_library",
        "//pkg/runtime/schema:go_default_library",
        "//pkg/util/cache:go_default_library",
        "//plugin/pkg/webhook:go_default_library",
        "//vendor:k8s.io/apiserver/pkg/authentication/authenticator",
        "//vendor:k8s.io/apiserver/pkg/authentication/user",
    ],
)

go_test(
    name = "go_default_test",
    srcs = [
        "certs_test.go",
        "webhook_test.go",
    ],
    library = ":go_default_library",
    tags = ["automanaged"],
    deps = [
        "//pkg/apis/authentication/v1beta1:go_default_library",
        "//pkg/apis/meta/v1:go_default_library",
        "//pkg/client/unversioned/clientcmd/api/v1:go_default_library",
        "//vendor:k8s.io/apiserver/pkg/authentication/user",
    ],
)

filegroup(
    name = "package-srcs",
    srcs = glob(["**"]),
    tags = ["automanaged"],
    visibility = ["//visibility:private"],
)

filegroup(
    name = "all-srcs",
    srcs = [":package-srcs"],
    tags = ["automanaged"],
)
