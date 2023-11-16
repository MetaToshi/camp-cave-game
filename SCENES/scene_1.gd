extends Node2D

func _process(_delta):
	if Input.is_action_pressed("SwapScene"):
		$Scene1Camera/Scene1Fader.visible = true
		$Scene1Camera/Scene1Fader/SCENE1FADER.play("Fade")

func _on_scene_1fader_animation_finished(anim_name):
	get_tree().change_scene_to_file("res://SCENES/scene_2.tscn")
