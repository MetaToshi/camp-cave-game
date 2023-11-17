extends Camera2D

@onready var camera = $"."

func _process(delta):
	print(camera.position)
	print(get_viewport().get_mouse_position())
	var j = get_viewport().get_mouse_position()
	if camera.position.x < 562:
		if j.x > 852:
			camera.position.x += (j.x - 852) * 0.02
	if camera.position.x > -562:
		if j.x < 400:
			camera.position.x -= (400 - j.x) * 0.02
