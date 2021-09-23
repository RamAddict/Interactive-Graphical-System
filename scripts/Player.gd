extends KinematicBody

const MOUSE_SENSITIVITY = 0.5
const MAX_SPEED = 20
const ACCEL = 5
const DEACCEL = 10
const GRAVITY = -10
const JUMP_SPEED = 8

var vel = Vector3()

onready var skeleton = $Skeleton
onready var body = $CollisionShapeBody
onready var feet = $CollisionShapeFeet
onready var camera = $Camera
onready var animator = $AnimationTree.get("parameters/playback")


func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)


func _input(event):
	# capture mouse
	if event is InputEventMouseButton and Input.get_mouse_mode() != Input.MOUSE_MODE_CAPTURED:
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	# rotation
	elif event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		var theta = deg2rad(event.relative.x * -MOUSE_SENSITIVITY)
		rotate_y(theta)
		skeleton.rotate_y(-theta)
		body.rotate_y(-theta)
		feet.rotate_y(-theta)


func _physics_process(delta):
	var dir = Vector3()

	# uncapture mouse
	if Input.is_action_just_pressed("ui_cancel"):
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

	# running
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

	# jumping / landing / falling
	if is_on_floor():
		if animator.get_current_node() == "Hop" or animator.get_current_node() == "Jump":
			animator.travel("Land")
		elif Input.is_action_just_pressed("movement_jump") and animator.get_current_node() != "Land":
			vel.y = JUMP_SPEED
			if movement.length() == 0:
				animator.travel("Hop")
			else:
				animator.travel("Jump")
		elif movement.length() == 0:
			animator.travel("Idle")
		else:
			animator.travel("Run")
	else:
		if animator.get_current_node() == "Run":
			animator.travel("Jump")
		elif animator.get_current_node() == "Idle":
			animator.travel("Hop")

	# compute movement
	dir.y = 0
	dir = dir.normalized()
	var target
	if is_on_floor():
		target = dir * MAX_SPEED
	else:
		target = dir * MAX_SPEED * 0.75

	# apply rotation
	if movement.length() > 0:
		var facing = skeleton.global_transform.basis.y.normalized()
		facing = Vector2(facing.x, -facing.z)
		var direction = Vector2(dir.x, -dir.z)
		var theta = facing.angle_to(direction)
		skeleton.rotate_y(theta * delta * ACCEL)

	# compute velocity
	var ground_velocity = Vector3(vel.x, 0, vel.z)
	var accel
	if dir.dot(ground_velocity) > 0 and is_on_floor():
		accel = ACCEL
	else:
		accel = DEACCEL
	ground_velocity = ground_velocity.linear_interpolate(target, accel * delta)

	# apply velocity
	vel.x = ground_velocity.x
	vel.z = ground_velocity.z
	vel.y += delta * GRAVITY
	vel = move_and_slide(vel, Vector3.UP)
