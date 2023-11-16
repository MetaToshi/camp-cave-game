extends Node2D



func _on_start_button_pressed():
	get_tree().change_scene_to_file("res://SCENES/scene_1.tscn")


func _on_options_button_pressed():
	get_tree().change_scene_to_file("res://SCENES/options.tscn")


func _on_quit_button_pressed():
	get_tree().quit()
