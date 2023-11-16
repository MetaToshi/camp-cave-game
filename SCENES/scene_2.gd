extends Node2D

func _process(_delta):
	if Input.is_action_pressed("SwapScene"):
		$Scene2Camera/Scene2Fader.visible = true
		$Scene2Camera/Scene2Fader/SCENE2FADER.play("Fade")

func _on_scene_2fader_animation_finished(anim_name):
	get_tree().change_scene_to_file("res://SCENES/main_scene.tscn")
