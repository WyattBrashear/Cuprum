extends Node2D
#Setup Neccasary Variables
@onready var squeak_label = $SqueaksLabel
@onready var squeaks: int = 0
@onready var squeak_label_text = "0"
@onready var dog_level: int = 0
@onready var dog_level_label = $DogLevel
@onready var squeaky_sprite = $Sprite2D
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	print("Is this thing on?")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_just_pressed("squeak"):
		squeaks = squeaks + 1
	squeak_label_text = "Squeaks: {squeaks}".format({"squeaks": squeaks})
	squeak_label.text = squeak_label_text
	
