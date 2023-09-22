#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xa78af5f3, "ioread32" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0x86ffe54a, "pci_iounmap" },
	{ 0x2aca3546, "pci_disable_device" },
	{ 0x881914cb, "pci_release_region" },
	{ 0x84f5e0d0, "pci_enable_device" },
	{ 0x174de1a6, "pci_read_config_word" },
	{ 0x7d11d264, "pci_read_config_byte" },
	{ 0x5921a19f, "pci_read_config_dword" },
	{ 0xee0bbc17, "pci_request_region" },
	{ 0x22af591a, "pci_iomap" },
	{ 0xa19b956, "__stack_chk_fail" },
	{ 0xdbef4a92, "__pci_register_driver" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0xeea3c1d8, "__class_create" },
	{ 0x32ab4392, "cdev_init" },
	{ 0x4c0ac327, "device_create" },
	{ 0x2dcc02c1, "cdev_add" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x9ec8f984, "pci_unregister_driver" },
	{ 0x6a2dd7c, "class_destroy" },
	{ 0x7e38d25d, "device_destroy" },
	{ 0xf7fb9e48, "cdev_del" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x122c3a7e, "_printk" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x4a453f53, "iowrite32" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0x453e7dc, "module_layout" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("pci:v00001172d00000004sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "4FA8BC6D22AFCAA9C8BE857");
