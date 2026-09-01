# Create a random 6-character suffix for unique resource names
# Get random strings for resource names
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}