extends Node2D


@onready var MainMenu = "res://SCENES/main_menu.tscn"
@onready var Scene1 = "res://SCENES/scene_1.tscn"
@onready var Scene2 = "res://SCENES/scene_2.tscn"



func _process(delta):
	get_tree().change_scene_to_file(MainMenu)
