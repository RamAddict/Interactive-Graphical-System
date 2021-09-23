extends KinematicBody

const MOUSE_SENSITIVITY = 0.5
const MAX_SPEED = 20
const ACCEL = 10
const DEACCEL = 15
const GRAVITY = -9.81
const JUMP_SPEED = 8

var dir = Vector3()
var vel = Vector3()

onready var body = $Skeleton
onready var camera = $Camera


func _init():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)


func _physics_process(delta):
	process_input(delta)
	process_movement(delta)


func _input(event):
	# capture mouse
	if event is InputEventMouseButton and Input.get_mouse_mode() != Input.MOUSE_MODE_CAPTURED:
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	# rotation
	elif event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		var theta = deg2rad(event.relative.x * -MOUSE_SENSITIVITY)
		rotate_y(theta)
		body.rotate_y(-theta)


func process_input(delta):
	# uncapture mouse
	if Input.is_action_just_pressed("ui_cancel"):
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

	# running
	dir = Vector3()
	var movement = Vector2()
	if Input.is_action_pressed("movement_forward"):
		movement.y += 1
	if Input.is_action_pressed("movement_backward"):
		movement.y -= 1
	if Input.is_action_pressed("movement_left"):
		movement.x -= 1
	if Input.is_action_pressed("movement_right"):
		movement.x += 1
	movement = movement.normalized()
	var cam = camera.global_transform
	dir += -cam.basis.z * movement.y
	dir += cam.basis.x * movement.x

	# jumping
	if is_on_floor():
		if Input.is_action_just_pressed("movement_jump"):
			vel.y = JUMP_SPEED


func process_movement(delta):
	dir.y = 0
	dir = dir.normalized()

	var ground_velocity = Vector3(vel.x, 0, vel.z)
	var target = dir * MAX_SPEED
	var accel
	if dir.dot(ground_velocity) > 0:
		accel = ACCEL
	else:
		accel = DEACCEL
	ground_velocity = ground_velocity.linear_interpolate(target, accel * delta)

	vel.x = ground_velocity.x
	vel.z = ground_velocity.z
	vel.y += delta * GRAVITY
	vel = move_and_slide(vel, Vector3.UP)
